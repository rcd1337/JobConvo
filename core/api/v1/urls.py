from django.urls import include, path
from rest_framework import routers
from .views import (
    JobListingViewSet,
    ReportViewSet,
)


router = routers.SimpleRouter()
router.register(r'job-listings', JobListingViewSet, basename='job-listings')

urlpatterns = [
    path('', include(router.urls)),
    path('report/', ReportViewSet.as_view(), name='report')
]
