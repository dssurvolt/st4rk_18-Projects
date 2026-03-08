from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Notary, TransactionFolio
from land_registry.models import Property
from django.contrib import messages
from .utils import notify_transaction_update
from django.utils import timezone
from functools import wraps

def notary_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not hasattr(request.user, 'notary_profile'):
            messages.error(request, "Accès réservé aux Notaires Certifiés.")
            return redirect('login_home')
        return view_func(request, *args, **kwargs)
    return _wrapped_view

@login_required
def web_choose_notary(request, property_id):
    """Étape 1 : L'acheteur choisit un notaire certifié."""
    prop = get_object_or_404(Property, id=property_id)
    notaries = Notary.objects.filter(is_verified=True).order_by('avg_processing_time_days')
    
    # Sécurité : On ne peut pas acheter son propre terrain
    if prop.owner_wallet == request.user:
        messages.error(request, "Vous ne pouvez pas initier une transaction sur votre propre propriété.")
        return redirect('web_property_detail', pk=property_id)

    return render(request, 'notaries/choose_notary.html', {
        'property': prop,
        'notaries': notaries
    })

@login_required
def web_start_transaction(request, property_id, notary_id):
    """Initialise le Folio de Transaction (Chaîne de valeur)."""
    prop = get_object_or_404(Property, id=property_id)
    notary = get_object_or_404(Notary, id=notary_id)
    
    # Vérifier s'il n'y a pas déjà une transaction en cours pour ce couple acheteur/propriété
    existing = TransactionFolio.objects.filter(
        property=prop, 
        buyer=request.user, 
        status__in=[TransactionFolio.Step.STEP1_NOTARY_SELECTED, TransactionFolio.Step.STEP2_ID_VERIFIED, TransactionFolio.Step.STEP3_DEED_SIGNED, TransactionFolio.Step.STEP4_ANDF_DEPOSITED, TransactionFolio.Step.STEP5_TITLE_MODIFIED]
    ).first()
    
    if existing:
        return redirect('web_transaction_status', folio_id=existing.id)

    # Création du folio
    folio = TransactionFolio.objects.create(
        property=prop,
        buyer=request.user,
        seller=prop.owner_wallet,
        notary=notary,
        status=TransactionFolio.Step.STEP1_NOTARY_SELECTED
    )
    
    messages.success(request, f"Dossier ouvert chez Me {notary.name}. Votre achat est maintenant sécurisé.")
    return redirect('web_transaction_status', folio_id=folio.id)

@login_required
def web_transaction_status(request, folio_id):
    """Suivi en temps réel de la transaction (Les 6 étapes)."""
    folio = get_object_or_404(TransactionFolio, id=folio_id)
    
    # Sécurité : Seules les parties ou le notaire peuvent voir
    if request.user not in [folio.buyer, folio.seller]:
        messages.error(request, "Accès non autorisé.")
        return redirect('login_home')

    return render(request, 'notaries/transaction_status.html', {
        'folio': folio,
        'steps': TransactionFolio.Step.choices,
        'current_step': folio.status
    })

@login_required
def user_transactions(request):
    """Liste de toutes les transactions de l'utilisateur (achats et ventes)."""
    purchases = TransactionFolio.objects.filter(buyer=request.user).order_by('-created_at')
    sales = TransactionFolio.objects.filter(seller=request.user).order_by('-created_at')
    
    return render(request, 'notaries/my_transactions.html', {
        'purchases': purchases,
        'sales': sales
    })

@login_required
@notary_required
def notary_dashboard(request):
    """Tableau de bord pour le notaire : liste des dossiers à traiter."""
    notary = request.user.notary_profile
    transactions = TransactionFolio.objects.filter(notary=notary).order_by('-updated_at')
    
    return render(request, 'notaries/notary_dashboard.html', {
        'notary': notary,
        'transactions': transactions
    })

@login_required
@notary_required
def update_transaction_step(request, folio_id):
    """Permet au notaire de valider une étape de la chaîne de valeur."""
    notary = request.user.notary_profile
    folio = get_object_or_404(TransactionFolio, id=folio_id, notary=notary)
    
    if request.method == 'POST':
        next_step = request.POST.get('next_step')
        andf_number = request.POST.get('andf_number')
        
        if next_step in dict(TransactionFolio.Step.choices):
            folio.status = next_step
            
            # Mise à jour des timestamps spécifiques
            now = timezone.now()
            if next_step == TransactionFolio.Step.STEP2_ID_VERIFIED:
                folio.step2_verified_at = now
            elif next_step == TransactionFolio.Step.STEP3_DEED_SIGNED:
                folio.step3_signed_at = now
            elif next_step == TransactionFolio.Step.STEP4_ANDF_DEPOSITED:
                folio.step4_deposited_at = now
                if andf_number:
                    folio.andf_dossier_number = andf_number
            elif next_step == TransactionFolio.Step.STEP5_TITLE_MODIFIED:
                folio.step5_modified_at = now
            elif next_step == TransactionFolio.Step.STEP6_COMPLETED:
                folio.step6_completed_at = now
                
            folio.save()
            
            # Déclencher les notifications (Email/SMS simulation)
            notify_transaction_update(folio)
            
            messages.success(request, f"Dossier mis à jour : {folio.get_status_display()}")
            
    return redirect('notary_dashboard')
