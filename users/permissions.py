from rest_framework import permissions


class HabitPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.user == request.user:
            return True
        if request.method in permissions.SAFE_METHODS:
            return obj.public_habit
        return False


class IsUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj:
            return True
        return False
