from rest_framework import serializers
from core.models import ApplicantProfile, JobListing, JobListingApplication
from accounts.models import Account


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
    applicants = JobListingApplicationSerializer(source='applications', many=True, read_only=True) # @TODO verificar 'applications' 
    
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
