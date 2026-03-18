from identity.models import User

def notary_context(request):
    """
    Fournit des informations globales sur le statut de notaire dans tous les templates.
    """
    if request.user.is_authenticated:
        is_notary = request.user.role == User.Role.NOTARY and hasattr(request.user, 'notary_profile')
        return {
            'is_notary': is_notary,
            'notary_profile': getattr(request.user, 'notary_profile', None) if is_notary else None
        }
    return {
        'is_notary': False,
        'notary_profile': None
    }
