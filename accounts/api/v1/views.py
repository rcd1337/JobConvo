from rest_framework import generics, permissions, status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from accounts.models import Account
from core.constants import Role
from .serializers import (
    AccountSerializer,
    ApplicationRegisterSerializer,
    RecruiterRegisterSerializer,
    CustomTokenObtainPairSerializer
)


class CustomTokenObtainPairView(TokenObtainPairView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CustomTokenObtainPairSerializer
    

class ApplicantRegister(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ApplicationRegisterSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        data["account_data"]["role"] = Role.APPLICANT
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RecruiterRegister(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RecruiterRegisterSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        data["account_data"]["role"] = Role.RECRUITER
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class UserViewSet(generics.ListAPIView):
    queryset = Account.objects.all().order_by("-id")
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]

