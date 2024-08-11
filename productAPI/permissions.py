from rest_framework.permissions import BasePermission, SAFE_METHODS

class ProductApiPermission(BasePermission):
    def has_permission(self, request, view):
        # Allow read-only permissions for any request
        if request.method in SAFE_METHODS:
            return True
        
        # Check for POST request and if the user belongs to admin or magazin groups
        if request.method in ['POST', 'PUT', 'DELETE']:
            print("here",request.user)
            return request.user and request.user.is_authenticated and (
                request.user.groups.filter(name="admin").exists() or 
                request.user.groups.filter(name="Magazin").exists()
            )
        
        return False
