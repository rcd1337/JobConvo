from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from accounts.models import Account
from core.models import ApplicantProfile, RecruiterProfile


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email

        return token


class AccountSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True, validators=[UniqueValidator(queryset=Account.objects.all())])
    email = serializers.EmailField(required=True,validators=[UniqueValidator(queryset=Account.objects.all())])
    password = serializers.CharField(write_only=True, required=True)
    role = serializers.CharField(required=False)

    def create(self, validated_data):
        account = Account(**validated_data)
        account.set_password(validated_data["password"])
        account.save()
        return account

    class Meta:
        model = Account
        fields = [
            "id",
            "username",
            "password",
            "email",
            "role",
        ]


class ApplicantProfileSerializer(serializers.ModelSerializer):
    account = serializers.PrimaryKeyRelatedField(queryset=Account.objects.all(), required=False, write_only=True)
    
    class Meta:
        model = ApplicantProfile
        fields = [
            "account",
            "salary_range_expectation",
            "experience",
            "educational_level",
        ]


class ApplicationRegisterSerializer(serializers.Serializer):
    account_data = AccountSerializer()
    applicant_profile_data = ApplicantProfileSerializer()

    def create(self, validated_data):
        account_data = validated_data.pop("account_data")
        applicant_profile_data = validated_data.pop("applicant_profile_data")
        
        # Create account
        account_serializer = AccountSerializer(data=account_data)
        account_serializer.is_valid(raise_exception=True)
        account = account_serializer.save()

        # Create applicant profile and associate with account
        recruiter_profile_data = ApplicantProfileSerializer(data=applicant_profile_data)
        recruiter_profile_data.is_valid(raise_exception=True)
        applicant_profile = recruiter_profile_data.save(account=account)
        
        return {
            'account_data': account,
            'applicant_profile_data': applicant_profile
        }


class RecruiterProfileSerializer(serializers.ModelSerializer):
    account = serializers.PrimaryKeyRelatedField(queryset=Account.objects.all(), required=False, write_only=True)
    
    class Meta:
        model = RecruiterProfile
        fields = [
            "account",
            "company_name"
        ]


class RecruiterRegisterSerializer(serializers.Serializer):
    account_data = AccountSerializer()
    recruiter_profile_data = RecruiterProfileSerializer()

    def create(self, validated_data):
        account_data = validated_data.pop("account_data")
        recruiter_profile_data = validated_data.pop("recruiter_profile_data")
        
        # Create account
        account_serializer = AccountSerializer(data=account_data)
        account_serializer.is_valid(raise_exception=True)
        account = account_serializer.save()

        # Create recruiter profile and associate with account
        recruiter_profile_data = RecruiterProfileSerializer(data=recruiter_profile_data)
        recruiter_profile_data.is_valid(raise_exception=True)
        recruiter_profile = recruiter_profile_data.save(account=account)
        
        return {
            'account_data': account,
            'recruiter_profile_data': recruiter_profile
        }
