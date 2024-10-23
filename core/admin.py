from django.contrib import admin
from . import models

admin.site.register(models.JobListing)
admin.site.register(models.Applicant)
admin.site.register(models.JobListingApplication)
