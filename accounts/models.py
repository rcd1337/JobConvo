from django.db import models
from django.contrib.auth.models import AbstractUser


# Choices
class Role(models.TextChoices):
    RECRUITER = "recruiter", "Recruiter"
    APPLICANT = "applicant", "Applicant"


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