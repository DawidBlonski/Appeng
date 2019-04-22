from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    message = "Not user."

    def has_object_permission(self, request, view, obj):
        return request.user == obj.current_user
