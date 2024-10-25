from django.db import models
from django.contrib.auth.models import AbstractUser
from core.constants import Role

# Models
class Account(AbstractUser):

    base_role = Role.APPLICANT

    role = models.CharField(
        max_length=64,
        choices=Role.choices,
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(null=False, blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, blank=True, auto_now=True)

    def __str__(self):
        return f"({self.id}) {self.username}"
