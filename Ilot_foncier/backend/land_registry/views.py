import json
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db.models import Count
from .models import Property, PropertyMedia
from identity.models import User
from consensus.models import ValidationRequest

# --- DASHBOARD VIEW (HTML) ---

def dashboard(request):
    """
    Tableau de bord principal pour l'administrateur / superviseur.
    """
    total_properties = Property.objects.count()
    raw_stats = {s['status']: s['count'] for s in Property.objects.values('status').annotate(count=Count('status'))}
    properties_by_status = []
    for status_code, status_label in Property.Status.choices:
        properties_by_status.append({
            'status': status_code,
            'count': raw_stats.get(status_code, 0)
        })
    
    total_users = User.objects.count()
    witnesses_count = User.objects.filter(role=User.Role.WITNESS).count()
    pending_validations = ValidationRequest.objects.filter(status=ValidationRequest.Status.OPEN).count()

    context = {
        'total_properties': total_properties,
        'properties_by_status': properties_by_status,
        'total_users': total_users,
        'witnesses_count': witnesses_count,
        'pending_validations': pending_validations,
    }
    return render(request, 'dashboard.html', context)

def user_dashboard(request, wallet):
    """
    Tableau de bord personnel pour un utilisateur.
    Affiche ses informations et ses parcelles.
    """
    try:
        user = User.objects.get(wallet_address=wallet)
        user_properties = Property.objects.filter(owner_wallet=user).annotate(media_count=Count('media'))
        
        context = {
            'user': user,
            'properties': user_properties,
            'total_assets': user_properties.count(),
        }
        return render(request, 'user_dashboard.html', context)
    except User.DoesNotExist:
        return render(request, 'user_dashboard.html', {'error': 'Utilisateur non trouvé'})

def web_properties(request):
    return render(request, 'properties.html')

def web_property_detail(request, pk):
    """Vue HTML détaillée pour une propriété spécifique."""
    try:
        prop = Property.objects.get(pk=pk)
        media = prop.media.all()
        return render(request, 'property_detail.html', {
            'property': prop,
            'media': media,
            'user': prop.owner_wallet
        })
    except Property.DoesNotExist:
        return render(request, 'property_detail.html', {'error': 'Propriété non trouvée'})

def web_profile(request, wallet):
    """Vue HTML pour le profil utilisateur."""
    try:
        user = User.objects.get(wallet_address=wallet)
        return render(request, 'profile.html', {'user': user})
    except User.DoesNotExist:
        return render(request, 'profile.html', {'error': 'Utilisateur non trouvé'})

def web_register_user(request):
    """Vue pour l'inscription combinée utilisateur + parcelle."""
    return render(request, 'register_user_property.html')

def web_login(request):
    """Vue pour la connexion citoyenne."""
    return render(request, 'login.html')

def web_password_reset(request):
    """Vue pour la réinitialisation de mot de passe."""
    return render(request, 'password_reset.html')

# --- API VIEWS (JSON) ---

@method_decorator(csrf_exempt, name='dispatch')
class PropertyListAPI(View):
    def get(self, request):
        properties = Property.objects.annotate(media_count=Count('media')).all()[:50]
        data = []
        for p in properties:
            owner_name = p.owner_wallet.full_name if p.owner_wallet.full_name else p.owner_wallet.wallet_address
            data.append({
                'id': str(p.id),
                'owner': owner_name,
                'status': p.status,
                'gps_centroid': p.gps_centroid,
                'media_count': p.media_count
            })
        return JsonResponse({'count': len(data), 'results': data})

    def post(self, request):
        try:
            if request.content_type.startswith('multipart/form-data'):
                data = request.POST
                files = request.FILES.getlist('files')
                gps_centroid = json.loads(data.get('gps_centroid', '{"lat":0, "lng":0}'))
                gps_boundaries = json.loads(data.get('gps_boundaries', '[]'))
                owner_wallet = data.get('owner_wallet')
                owner_name = data.get('owner_name')
            else:
                body = json.loads(request.body)
                owner_wallet = body.get('owner_wallet')
                owner_name = body.get('owner_name')
                gps_centroid = body.get('gps_centroid', {'lat': 0, 'lng': 0})
                gps_boundaries = body.get('gps_boundaries', [])
                files = []

            if not owner_wallet or not owner_name:
                return JsonResponse({'error': 'owner_wallet and owner_name required'}, status=400)
            
            # 1. Vérification des Doublons (Coordonnées)
            # On vérifie si une parcelle existe déjà à ces coordonnées exactes (centroid)
            lat = float(gps_centroid.get('lat', 0))
            lng = float(gps_centroid.get('lng', 0))
            
            # Simulation de recherche spatiale simple (même point ou très proche)
            # Dans un vrai système on utiliserait PostGIS ST_DWithin
            existing = Property.objects.filter(
                gps_centroid__lat__gte=lat-0.0001, 
                gps_centroid__lat__lte=lat+0.0001,
                gps_centroid__lng__gte=lng-0.0001,
                gps_centroid__lng__lte=lng+0.0001
            ).exists()
            
            if existing:
                return JsonResponse({'error': 'Une parcelle est déjà enregistrée à ces coordonnées.'}, status=409)

            # Validation du nom
            import re
            if not re.match(r"^[a-zA-Z\s\.\-]+$", owner_name) or len(owner_name) < 3:
                return JsonResponse({'error': 'Nom invalide'}, status=400)
            
            owner, _ = User.objects.get_or_create(wallet_address=owner_wallet)
            owner.full_name = owner_name
            owner.save()
            
            if not (-90 <= lat <= 90) or not (-180 <= lng <= 180):
                return JsonResponse({'error': 'GPS hors plage'}, status=400)
            
            prop = Property.objects.create(
                owner_wallet=owner,
                gps_centroid=gps_centroid,
                gps_boundaries=gps_boundaries,
                status=Property.Status.DRAFT
            )

            # Sauvegarde des médias
            import hashlib
            for f in files:
                content = f.read()
                fake_cid = "Qm" + hashlib.sha256(content).hexdigest()[:44]
                m_type = PropertyMedia.MediaType.OTHER_MEDIA
                if f.content_type.startswith('image/'): m_type = PropertyMedia.MediaType.PHOTO_LAND
                elif f.content_type.startswith('video/'): m_type = PropertyMedia.MediaType.VIDEO_DRONE
                elif f.content_type == 'application/pdf': m_type = PropertyMedia.MediaType.LEGAL_DOC

                PropertyMedia.objects.create(property=prop, ipfs_cid=fake_cid, media_type=m_type)

            return JsonResponse({'id': str(prop.id), 'status': prop.status}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

@method_decorator(csrf_exempt, name='dispatch')
class PropertyDetailAPI(View):
    """
    API Endpoint: /api/properties/<uuid>/
    GET: Détails d'une propriété
    """
    def get(self, request, pk):
        try:
            p = Property.objects.get(pk=pk)
            data = {
                'id': str(p.id),
                'owner': p.owner_wallet.wallet_address,
                'status': p.status,
                'gps_centroid': p.gps_centroid,
                'gps_boundaries': p.gps_boundaries,
                'on_chain_id': p.on_chain_id
            }
            return JsonResponse(data)
        except Property.DoesNotExist:
            return JsonResponse({'error': 'Not found'}, status=404)
