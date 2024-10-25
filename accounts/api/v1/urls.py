from django.urls import path
from .views import ApplicantRegister, RecruiterRegister, UserViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenVerifyView
)

urlpatterns = [
    path("register-applicant/", ApplicantRegister.as_view(), name="register-applicant"),
    path("register-recruiter/", RecruiterRegister.as_view(), name="register-recruiter"),
    path("users/", UserViewSet.as_view(), name="users"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
