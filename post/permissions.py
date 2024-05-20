from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """
    Permission for check Post owner
    """

    def has_object_permission(self, request, view, obj):
        if request.user == obj.author:
            return request.method in ('PATCH', 'DELETE', )
        return False
