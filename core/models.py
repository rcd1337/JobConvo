from django.db import models
from accounts.models import Account


# Choices
class SalaryRangeChoices(models.TextChoices):
    UP_TO_1000 = "up_to_1000", "Up to 1000"
    FROM_1001_TO_2000 = "from_1001_to_2000", "From 1001 to 2000"
    FROM_2001_TO_3000 = "from_2001_to_3000", "From 2001 to 3000"
    ABOVE_3000 = "above_3000", "Above 3000"

class EducationChoices(models.TextChoices):
    ELEMENTARY = "elementary", "Ensino Fundamental"
    HIGH_SCHOOL = "high_school", "Ensino médio"
    TECHNOGIST = "technologist", "Tecnólogo"
    BACHELORS = "bachelors", "Ensino Superior"
    POSTGRADUATE = "postgraduate", "Pós / MBA / Mestrado"
    DOCTORATE = "doctorate", "Doutorado"


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
    created_at = models.DateTimeField(null=False, blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, blank=True, auto_now=True)
    
    def __str__(self):
        return self.title


class Applicant(models.Model):
    
    account = models.OneToOneField(
        Account,
        on_delete=models.CASCADE,
        related_name="application_details",
        null=False,
        blank=False,
    )
    salary_expectation = models.CharField(
        max_length=64,
        choices=SalaryRangeChoices.choices,
        null=False,
        blank=False
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
    created_at = models.DateTimeField(null=False, blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, blank=True, auto_now=True)
    
    def __str__(self):
        return self.account.username
    

class JobListingApplication(models.Model):
    applicant = models.ForeignKey(
        Applicant,
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
    applicant_ranking = ()
    created_at = models.DateTimeField(null=False, blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, blank=True, auto_now=True)
    
    def __str__(self):
        return f"{self.applicant} applied to {self.job_listing}"
    