from django.urls import path
from .views import Register, UserViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenVerifyView
)

urlpatterns = [
    path("register/", Register.as_view(), name="register"),
    path("users/", UserViewSet.as_view(), name="users"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
