from rest_framework.permissions import BasePermission
from accounts.enums import UserRole


class IsClient(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == UserRole.CLIENT.value
    
    def has_object_permission(self, request, view, obj):
        return request.role == UserRole.CLIENT.value