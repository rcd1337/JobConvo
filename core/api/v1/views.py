from datetime import datetime
from rest_framework import viewsets, generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError, APIException
from rest_framework.decorators import action
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
    queryset = JobListing.objects.all()
    
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


class ReportViewSet(generics.GenericAPIView):
    serializer_class = ReportSerializer
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        year = request.query_params.get("year")
        month = request.query_params.get("month")
        
        if not year and not month:
            year = datetime.now().year
            month = datetime.now().month
        
        # Validate both variables were informed in the request
        if not year or not month:
            raise APIException("You must inform year and month, e.g.: ...report/?year=2000&?month=11")

        # Validate year and month
        try:
            datetime(int(year), int(month), 1)
        except ValueError:
            raise APIException("Invalid date. Please provide a valid year(e.g.: 2000) and month (1-12).")
        
        job_listings_count = count_montly_entries(model=JobListing, year=year, month=month),
        applications_count = count_montly_entries(model=JobListingApplication, year=year, month=month)
        
        data = {
            "job_listings_amount": job_listings_count,
            "applications_amount": applications_count
        }

        serializer = self.get_serializer(data)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
