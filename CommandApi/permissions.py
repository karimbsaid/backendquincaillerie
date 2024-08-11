from rest_framework.permissions import BasePermission

class IsAdminOrMagazinOrReadOnly(BasePermission):
    """
    Custom permission to only allow users in 'admin' or 'magazin' groups to read commands.
    """
    def has_permission(self, request, view):
        # Allow any user to create (POST) commands
        if request.method in ('POST',):
            return True
        # Only allow users in 'admin' or 'magazin' groups to read (GET) commands
        if request.method in ('GET',):
            return request.user and request.user.is_authenticated and (
                request.user.groups.filter(name='admin').exists() or
                request.user.groups.filter(name='Magazin').exists()
            )
        # Allow authenticated users for other methods
        return request.user and request.user.is_authenticated
