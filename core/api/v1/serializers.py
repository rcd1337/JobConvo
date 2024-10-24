from rest_framework import serializers
from core.models import Account, Applicant, JobListing, JobListingApplication


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "role",
        ]


class ApplicantSerializer(serializers.ModelSerializer):
    account = AccountSerializer(required=False, read_only=True)
    
    def create(self, validated_data):
        return super().create(validated_data)
    
    class Meta:
        model = Applicant
        fields = [
            "id",
            "account",
            "salary_range_expectation",
            "experience",
            "educational_level",
        ]


class JobListingSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.update({
            "number_of_applicants": instance.applications.count()
        })
        return data
    
    class Meta:
        model = JobListing
        fields = [
            "id",
            "title",
            "requirements",
            "min_educational_level",
            "salary_range",
            "created_at",
            "updated_at",
        ]


class JobListingApplicationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = JobListingApplication
        fields = [
            "id",
            "job_listing",
            "applicant",
            "created_at",
        ]


class JobListingRetrieveSerializer(serializers.ModelSerializer):
    applicants = JobListingApplicationSerializer(source='applications', many=True, read_only=True)
    
    class Meta:
        model = JobListing
        fields = [
            "id",
            "title",
            "requirements",
            "min_educational_level",
            "created_at",
            "updated_at",
            "applicants"
        ]


class ReportSerializer(serializers.Serializer):
    job_listings_amount = serializers.IntegerField()
    applications_amount = serializers.IntegerField()
