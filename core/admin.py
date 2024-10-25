from django.contrib import admin
from . import models

admin.site.register(models.JobListing)
admin.site.register(models.ApplicantProfile)
admin.site.register(models.RecruiterProfile)
admin.site.register(models.JobListingApplication)
