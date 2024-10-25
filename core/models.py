from django.db import models
from accounts.models import Account
from .constants import SalaryRangeChoices, EducationChoices
from .utils import calculate_applicant_ranking


# Models
class JobListing(models.Model):
    title = models.CharField(
        max_length=128,
        null=False,
        blank=False,
    )
    requirements = models.TextField(
        null=False,
        blank=False,
    )
    min_educational_level = models.CharField(
        max_length=64,
        choices=EducationChoices.choices,
        null=False,
        blank=False,
    )
    salary_range = models.CharField(
        max_length=64,
        choices=SalaryRangeChoices.choices,
        null=False,
        blank=False
    )
    recruiter = models.ForeignKey(
        Account,
        on_delete=models.SET_NULL,
        related_name="job_listings",
        null=True,
        blank=False,
    )
    created_at = models.DateTimeField(null=False, blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, blank=True, auto_now=True)
    
    def __str__(self):
        return f"({self.id}) {self.title}"


class ApplicantProfile(models.Model):
    
    account = models.OneToOneField(
        Account,
        on_delete=models.CASCADE,
        related_name="applicant_profile",
        null=False,
        blank=False,
    )
    experience = models.TextField(
        null=False,
        blank=False,
    )
    educational_level = models.CharField(
        max_length=64,
        choices=EducationChoices.choices,
        null=False,
        blank=False,
    )
    salary_range_expectation = models.CharField(
        max_length=64,
        choices=SalaryRangeChoices.choices,
        null=False,
        blank=False
    )
    created_at = models.DateTimeField(null=False, blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, blank=True, auto_now=True)
    
    def __str__(self):
        return f"({self.id}) {self.account.username}"


class RecruiterProfile(models.Model):
    
    account = models.OneToOneField(
        Account,
        on_delete=models.CASCADE,
        related_name="recruiter_profile",
        null=False,
        blank=False,
    )
    company_name = models.CharField(
        max_length=64,
        null=False,
        blank=False,
    )
    created_at = models.DateTimeField(null=False, blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, blank=True, auto_now=True)
    
    def __str__(self):
        return f"({self.id}) {self.account.username}"


class JobListingApplication(models.Model):
    applicant = models.ForeignKey(
        Account,
        on_delete=models.SET_NULL,
        related_name="applications",
        null=True,
        blank=False,
    )
    job_listing = models.ForeignKey(
        JobListing,
        on_delete=models.CASCADE,
        related_name="applications",
        null=False,
        blank=False,
    )
    applicant_ranking = models.IntegerField(
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(null=False, blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, blank=True, auto_now=True)
    
    def save(self, *args, **kwargs):
        self.applicant_ranking = calculate_applicant_ranking(
            applicant_educational_level=self.applicant.applicant_profile.educational_level,
            applicant_salary_range_expectation=self.applicant.applicant_profile.salary_range_expectation,
            job_listing_min_educational_level=self.job_listing.min_educational_level,
            job_listing_salary_range=self.job_listing.salary_range
        )
        return super().save(*args, **kwargs)
        
    def __str__(self):
        return f"({self.id}) {self.applicant.username} applied to {self.job_listing.title}"
