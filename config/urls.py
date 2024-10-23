from django.contrib import admin
from django.urls import include, path


apps_urlpattenrs = [
    path('', include('core.urls')),
    path('', include('accounts.urls')),
]

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Apps
    *apps_urlpattenrs
]
