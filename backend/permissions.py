from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions always allowed
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Write perms only allowed to owner of object
        if hasattr(obj, 'user_id'):
            return obj.user == request.user
        elif hasattr(obj, 'profile'):
            return obj.profile == request.user
        
        return False