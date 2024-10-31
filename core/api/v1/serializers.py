from rest_framework import serializers
from core.models import JobListing, JobListingApplication
from accounts.models import Account

class NestedAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = [
            "username",
            "email",
            "role",
        ]
        read_only_fieds = [*fields]
    

class JobListingSerializer(serializers.ModelSerializer):
    recruiter = NestedAccountSerializer(required=False)
    
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
            "recruiter",
            "created_at",
            "updated_at",
        ]


class JobListingApplicationSerializer(serializers.ModelSerializer):
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.update({
            "applicant_email": instance.applicant.email
        })
        return data
    
    class Meta:
        model = JobListingApplication
        fields = [
            "id",
            "job_listing",
            "applicant",
            "applicant_ranking",
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
            "recruiter",
            "created_at",
            "updated_at",
            "applicants"
        ]


class ReportSerializer(serializers.Serializer):
    job_listings_amount = serializers.IntegerField()
    applications_amount = serializers.IntegerField()
