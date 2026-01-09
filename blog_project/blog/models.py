"""
Database models for the blog application.

Defines:
- UserProfile: Extended user information
- BlogPost: Individual blog posts with author, title, content, timestamps
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class UserProfile(models.Model):
    """
    Extended user profile model.
    
    Maps to Figma: User Avatar Component (Circular shape)
    Stores additional user information beyond Django's built-in User model.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=500, blank=True, default='')
    avatar_url = models.URLField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'


class BlogPost(models.Model):
    """
    Blog post model.
    
    Maps to Figma: Blog Card Component (Square shape with content)
    Represents individual blog articles with author, title, content, and metadata.
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    excerpt = models.CharField(max_length=300, blank=True, default='')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)
    views_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'

    def get_excerpt(self):
        """Return excerpt or first 300 characters of content."""
        return self.excerpt or self.content[:300] + '...'
