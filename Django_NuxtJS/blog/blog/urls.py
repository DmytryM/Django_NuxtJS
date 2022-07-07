from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('myblog.urls')),
    path('admin/', admin.site.urls),
]