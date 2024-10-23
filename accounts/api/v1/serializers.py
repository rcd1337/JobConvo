from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from accounts.models import Account    


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email

        return token


class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True, 
        validators=[UniqueValidator(queryset=Account.objects.all())]
    )
    password = serializers.CharField(
        write_only=True, 
        required=True
    )
    email = serializers.EmailField(required=True, 
        validators=[UniqueValidator(queryset=Account.objects.all())]
    )

    def create(self, validated_data):
        user = Account.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
        )

        user.set_password(validated_data["password"])
        user.save()

        return user
    
    class Meta:
        model = Account
        fields = [
            "username",
            "email", 
            "password"
        ]


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Account
        fields = "__all__"
