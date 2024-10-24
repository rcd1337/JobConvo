from rest_framework import viewsets, mixins, generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import action
from datetime import datetime
from core.models import (
    JobListing,
    JobListingApplication,
    Applicant
)
from .serializers import (
    JobListingSerializer,
    JobListingApplicationSerializer,
    JobListingRetrieveSerializer,
    ReportSerializer,
    ApplicantSerializer
)


# @TODO permissions
# @TODO implement swagger
class JobListingViewSet(viewsets.ModelViewSet):
    queryset = JobListing.objects.all()
    permission_classes = [AllowAny]
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return JobListingRetrieveSerializer
        if self.action == 'apply_to_job':
           return JobListingApplicationSerializer
        return JobListingSerializer
    
    
    # Enables applicants to apply for a job listing
    @action(
        detail=True,
        permission_classes=permission_classes,
        methods=["POST"],
        url_path="apply_to_job"
    )
    def apply_to_job(self, request, **kwargs):
        applicant = getattr(self.request.user, "applicant", None)
        job_listing = self.get_object()
        data = request.data
        
        # Provides aditional data to the serializer
        data.update({
            "applicant": applicant.id,
            "job_listing":job_listing.id,
        })
        
        # Validates if user account has it's applicant profile information
        if not applicant:
            raise ValidationError("You can not perform this action because your applicant profile doesn't exist.")
        
        # Validates if user has already applied for this job listing
        if job_listing.applications.filter(applicant=applicant).exists():
            raise ValidationError("You have already applied for this job listing.")
        
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(
            {"detail": "You have successfully applied for this job."},
            status=status.HTTP_200_OK
        )


class ApplicantViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin
):
    queryset = Applicant
    permission_classes = [AllowAny]
    serializer_class = ApplicantSerializer
    
    def perform_create(self, serializer):
        user = self.request.user
        # Validates user has no applicant profile associated to his account yet
        if hasattr(user, "applicant"):
            raise ValidationError("You can not create an applicant profile because your account already has one")
        return serializer.save(account=user)
        
    
    def perform_update(self, serializer):
        # Validates applicant profile is being update by the right user account
        if not self.request.user == serializer.instance.account:
            raise ValidationError("You are not allowed to perfom this action")
        return super().perform_update(serializer)


class ReportViewSet(generics.GenericAPIView):
    serializer_class = ReportSerializer
    
    def get(self, request, *args, **kwargs):
        year = request.query_params.get("year", datetime.now().year)
        month = request.query_params.get("month", datetime.now().year)
        
        # @TODO validador year/month
        # @TODO separar count numa função
        # @TODO utilizar django filters
        
        if year and month:
            job_listings_count = JobListing.objects.filter(
                created_at__year=year,
                created_at__month=month
            ).count()
            
            applications_count = JobListingApplication.objects.filter(
                created_at__year=year,
                created_at__month=month
            ).count()
        
        data = {
            "job_listings_amount": job_listings_count,
            "applications_amount":applications_count
        }

        serializer = self.get_serializer(data)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
