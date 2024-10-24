from django.urls import include, path
from rest_framework import routers
from .views import (
    JobListingViewSet,
    ReportViewSet,
    ApplicantViewSet,
)


router = routers.SimpleRouter()
router.register(r'job-listings', JobListingViewSet, basename='job-listings')
router.register(r'applicants', ApplicantViewSet, basename='applicants')

urlpatterns = [
    path('', include(router.urls)),
    path('report/', ReportViewSet.as_view(), name='report')
]
