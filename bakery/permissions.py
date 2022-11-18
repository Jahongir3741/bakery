from rest_framework.permissions import BasePermission
from accounts.enums import UserRole


METHOD = ['POST', 'PUT', 'PATCH', 'DELETE']


# IsOwner permission
class IsOwner(BasePermission):
    def has_permission(self, request, view):
        if not request.user.type.is_director and request.method in METHOD:
            return False
        return True
    
    def has_object_permission(self, request, view, obj):
        if not request.user == obj.owner and request.method in METHOD:
            return False
        return True


class IsDirectorOrVendor(BasePermission):
    def has_permission(self, request, view):
        if not (request.user.is_director or request.user.is_vendor) and request.method in METHOD:
            return False
        return True
    
    def has_object_permission(self, request, view, obj):
        
        return super().has_object_permission(request, view, obj)


class IsNotClientPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.role != UserRole.CLIENT.value


class IsClient(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == UserRole.CLIENT.value