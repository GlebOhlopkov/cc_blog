from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """
    Permission for check Comment owner
    """

    def has_object_permission(self, request, view, obj):
        if request.user == obj.autor:
            return request.method in ('PATCH', 'DELETE', )
        return False
