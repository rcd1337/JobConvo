from typing import Iterable
from django.db import models
from accounts.models import Account


# Choices
class EducationChoices(models.TextChoices):
    ELEMENTARY = "elementary", "Ensino Fundamental"
    HIGH_SCHOOL = "high_school", "Ensino médio"
    TECHNOGIST = "technologist", "Tecnólogo"
    BACHELORS = "bachelors", "Ensino Superior"
    POSTGRADUATE = "postgraduate", "Pós / MBA / Mestrado"
    DOCTORATE = "doctorate", "Doutorado"
    
class SalaryRangeChoices(models.TextChoices):
    UP_TO_1000 = "up_to_1000", "Up to 1000"
    FROM_1001_TO_2000 = "from_1001_to_2000", "From 1001 to 2000"
    FROM_2001_TO_3000 = "from_2001_to_3000", "From 2001 to 3000"
    ABOVE_3000 = "above_3000", "Above 3000"


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
        related_name="applicant",
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
        return f"{self.id} - {self.account.username}"
    

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
    applicant_ranking = models.IntegerField(
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(null=False, blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, blank=True, auto_now=True)
    
    def save(self, *args, **kwargs):

        self.applicant_ranking = self.calculate_applicant_ranking(
            applicant_educational_level=self.applicant.educational_level,
            applicant_salary_range_expectation=self.applicant.salary_range_expectation,
            job_listing_min_educational_level=self.job_listing.min_educational_level,
            job_listing_salary_range=self.job_listing.salary_range
        )
        return super().save(*args, **kwargs)
    
    
    def calculate_applicant_ranking(
        self,
        applicant_educational_level,
        applicant_salary_range_expectation, 
        job_listing_min_educational_level,
        job_listing_salary_range,
        ):
        min_educational_level = {
            EducationChoices.ELEMENTARY : 0,
            EducationChoices.HIGH_SCHOOL : 1,
            EducationChoices.TECHNOGIST : 2,
            EducationChoices.BACHELORS : 3,
            EducationChoices.POSTGRADUATE : 4,
            EducationChoices.DOCTORATE : 5,
        }
        salary_range_dict = {
            SalaryRangeChoices.UP_TO_1000 : 0,
            SalaryRangeChoices.FROM_1001_TO_2000 : 1,
            SalaryRangeChoices.FROM_2001_TO_3000 : 2,
            SalaryRangeChoices.ABOVE_3000 : 3,
        }
        applicant_education_value = min_educational_level.get(applicant_educational_level)
        applicant_salary_value = salary_range_dict.get(applicant_salary_range_expectation)
        job_listing_education_value = min_educational_level.get(job_listing_min_educational_level)
        job_listing_salary_value = salary_range_dict.get(job_listing_salary_range)
        ranking = 0
        if applicant_education_value <= job_listing_education_value:
            ranking +=1
        if applicant_salary_value <= job_listing_salary_value:
            ranking += 1
        return ranking
        
    def __str__(self):
        return f"{self.applicant} applied to {self.job_listing}"
    
    