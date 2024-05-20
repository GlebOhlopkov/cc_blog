from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='admin').exists()


class IsOwnerYourself(BasePermission):
    """
    Permission for check User is itself
    """

    def has_object_permission(self, request, view, obj):
        if request.user == obj:
            return request.method in ('PATCH',)
        return False
