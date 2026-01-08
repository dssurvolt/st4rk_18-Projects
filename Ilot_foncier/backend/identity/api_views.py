from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import User

@method_decorator(csrf_exempt, name='dispatch')
class UserProfileAPI(View):
    """
    API Endpoint: /api/identity/profile/<wallet>/
    GET: Récupère le profil public (Rôle, Réputation)
    """
    def get(self, request, wallet):
        try:
            user = User.objects.get(wallet_address=wallet)
            data = {
                'wallet_address': user.wallet_address,
                'role': user.role,
                'reputation_score': user.reputation_score,
                'is_active': user.is_active,
                'date_joined': user.date_joined.isoformat()
            }
            return JsonResponse(data)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
