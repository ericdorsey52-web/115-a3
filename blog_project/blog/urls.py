"""
URL routing for blog application.

Maps URLs to views for:
- Sign Up (GET/POST)
- Log In (GET/POST)
- Log Out
- Blog Homepage
- Blog Detail
- Create Post
- About

Follows Django URL naming conventions for easy reference in templates.
"""

from django.urls import path
from . import views

urlpatterns = [
    # Authentication URLs
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # Blog URLs
    path('', views.home_view, name='home'),
    path('post/<int:post_id>/', views.blog_detail_view, name='blog_detail'),
    path('create/', views.create_blog_view, name='create_blog'),
    
    # Static Pages
    path('about/', views.about_view, name='about'),
]
