from rest_framework.permissions import BasePermission
from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied
from rest_framework import permissions
class IsDeliveryMan(BasePermission):
    """
    Allows access only to users with role='delivery'
    """
    message = "This API can be accessed only by delivery man"

    def has_permission(self, request, view):
        if request.user.role != 'delivery':
            raise PermissionDenied(detail=self.message)
        return True
    
class IsDeliveryMans(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'delivery'
    
    
class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'