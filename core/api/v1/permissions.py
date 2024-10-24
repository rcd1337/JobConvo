from rest_framework.permissions import BasePermission
from accounts.models import Role

# Custom permission classes
class IsRecruiter(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == Role.RECRUITER

class IsApplicant(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == Role.APPLICANT
