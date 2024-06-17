from rest_framework.permissions import SAFE_METHODS, BasePermission
from rest_framework.request import Request
from rest_framework.views import APIView
from contents.models import Content


class IsUserOnCourseByContent(BasePermission):
    def has_object_permission(self, request: Request, view: APIView, obj: Content):
        if request.method in SAFE_METHODS:
            return (
                request.user in obj.course.students.all() or request.user.is_superuser
            )
        return request.user.is_superuser


class IsSuperuser(BasePermission):
    def has_permission(self, request: Request, view: APIView):
        return request.user.is_superuser
