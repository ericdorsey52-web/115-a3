"""
URL configuration for blog_project.

Maps routes to views for Sign Up, Log In, and Blog homepage.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # Include blog app URLs
]
