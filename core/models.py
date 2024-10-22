from django.contrib.auth.models import AbstractUser
from django.db import models


# Choices
class Role(models.TextChoices):
    RECRUITER = "recruiter", "Recruiter"
    APPLICANT = "applicant", "Candidato"

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
class Account(AbstractUser):

    base_role = Role.APPLICANT

    role = models.CharField(
        max_length=64,
        choices=Role.choices,
        default=Role.APPLICANT,
        null=False,
        blank=False,
    )
    created_at = models.DateTimeField(null=False, blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, blank=True, auto_now=True)

    def __str__(self):
        return self.username


class JobListnig(models.Model):

    title = models.CharField(
        max_length=128,
        null=False,
        blank=False,
    )
    requirements = models.TextField(
        null=False,
        blank=False,
    )
    education = models.CharField(
        max_length=64,
        choices=EducationChoices.choices,
        null=False,
        blank=False,
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
    salary_expectation = models.DecimalField(
        max_digits=12,
        decimal_places=2,
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