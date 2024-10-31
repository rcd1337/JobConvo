from datetime import datetime
from rest_framework import viewsets, generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError, APIException
from rest_framework.decorators import action
from django.db.models import Prefetch
from core.utils import count_montly_entries
from core.models import (
    JobListing,
    JobListingApplication,
)
from .permissions import IsRecruiter, IsApplicant
from .serializers import (
    JobListingSerializer,
    JobListingApplicationSerializer,
    JobListingRetrieveSerializer,
    ReportSerializer,
)


class JobListingViewSet(viewsets.ModelViewSet):
    queryset = JobListing.objects.prefetch_related(
        Prefetch('applications', queryset=JobListingApplication.objects.all().order_by('-applicant_ranking'))
    )
    
    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            permission_classes = [IsRecruiter]
        elif self.action in ["apply_to_job"]:
            permission_classes = [IsApplicant]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return JobListingRetrieveSerializer
        if self.action == 'apply_to_job':
           return JobListingApplicationSerializer
        return JobListingSerializer
    
    def perform_create(self, serializer):
        recruiter = self.request.user
        serializer.save(recruiter=recruiter)
        return super().perform_create(serializer)
    
    
    
    # Enable applicants to apply for a job listing
    @action(
        detail=True,
        permission_classes=[IsApplicant],
        methods=["POST"],
        url_path="apply_to_job"
    )
    def apply_to_job(self, request, **kwargs):
        applicant = request.user
        job_listing = self.get_object()
        data = request.data

        data.update({
            "applicant": applicant.id,
            "job_listing":job_listing.id,
        })
        
        # Validate if user account has it's applicant profile information
        if not hasattr(applicant, "applicant_profile"):
            raise ValidationError("Your account can not perform this action. Applicant profile is missing")
        
        # Validate if user has already applied for this job listing
        if job_listing.applications.filter(applicant=applicant).exists():
            raise ValidationError("You have already applied for this job listing.")
        
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(
            {"detail": "You have successfully applied for this job."},
            status=status.HTTP_200_OK
        )


class ReportView(generics.GenericAPIView):
    serializer_class = ReportSerializer
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        
        # Return total entries count.
        if not request.query_params:
            data = {
                "job_listings_amount": count_montly_entries(JobListing),
                "applications_amount": count_montly_entries(JobListingApplication)
            }
            serializer = self.get_serializer(data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        # Return given period entries count.
        year = request.query_params.get("year")
        month = request.query_params.get("month")
        
        # Validate year and month.
        try:
            datetime(int(year), int(month), 1)
        except (ValueError, TypeError):
            raise APIException("Invalid date. Provide a valid year and month (e.g.: .../report/?year=2000&month=1).")
        
        data = {
            "job_listings_amount": count_montly_entries(model=JobListing, year=year, month=month),
            "applications_amount": count_montly_entries(model=JobListingApplication, year=year, month=month)
        }
        serializer = self.get_serializer(data)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
