"""
View functions for handling user authentication and blog interactions.

Maps to Figma:
- Sign Up Page → signup_view
- Log In Page → login_view
- Blog Homepage → home_view

User Stories Addressed:
1. "As a new user, I want to create an account easily" → signup_view
2. "As a returning user, I want to log in quickly" → login_view
3. "As a user, I want clear and simple input fields" → All forms with proper labels
"""

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from .forms import UserSignUpForm, UserLoginForm, BlogPostForm
from .models import BlogPost


@require_http_methods(["GET", "POST"])
def signup_view(request):
    """
    Handle user registration (Sign Up).
    
    GET: Displays the Sign Up form
    POST: Processes form submission and creates new user account
    
    User Story: "As a new user, I want to create an account easily"
    Figma Mapping: Sign Up page with input fields and submit button
    """
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Automatically log in the user after registration
            login(request, user)
            messages.success(request, 'Account created successfully! Welcome!')
            return redirect('home')
        else:
            # Form errors will be displayed in template
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = UserSignUpForm()
    
    return render(request, 'auth/signup.html', {
        'form': form,
        'page_title': 'Sign Up'
    })


@require_http_methods(["GET", "POST"])
def login_view(request):
    """
    Handle user login.
    
    GET: Displays the Log In form
    POST: Authenticates user and creates session
    
    User Story: "As a returning user, I want to log in quickly"
    Figma Mapping: Log In page with email/username and password fields
    """
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            # Authenticate user
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully!')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = UserLoginForm()
    
    return render(request, 'auth/login.html', {
        'form': form,
        'page_title': 'Log In'
    })


@require_http_methods(["GET"])
def logout_view(request):
    """
    Handle user logout.
    
    Clears user session and redirects to home.
    """
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('home')


def home_view(request):
    """
    Display blog homepage with list of blog posts.
    
    Shows:
    - All published blog posts
    - Post cards with title, author, excerpt, date
    - Links to read full posts
    
    User Story: "As a user, I want clear and simple input fields"
    This is reflected in the blog post list display with clear hierarchy
    """
    blog_posts = BlogPost.objects.filter(published=True).order_by('-created_at')
    
    context = {
        'page_title': 'Blog',
        'blog_posts': blog_posts,
    }
    
    return render(request, 'blog/home.html', context)


@login_required(login_url='login')
def blog_detail_view(request, post_id):
    """
    Display a single blog post in detail.
    
    Shows full content, author info, and timestamps.
    Requires user to be logged in.
    """
    try:
        post = BlogPost.objects.get(id=post_id, published=True)
        post.views_count += 1
        post.save()
    except BlogPost.DoesNotExist:
        messages.error(request, 'Blog post not found.')
        return redirect('home')
    
    context = {
        'page_title': post.title,
        'post': post,
    }
    
    return render(request, 'blog/detail.html', context)


@login_required(login_url='login')
def create_blog_view(request):
    """
    Allow logged-in users to create new blog posts.
    
    Maps to Figma: Blog creation form
    """
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Blog post created successfully!')
            return redirect('home')
    else:
        form = BlogPostForm()
    
    context = {
        'page_title': 'Create Post',
        'form': form,
    }
    
    return render(request, 'blog/create.html', context)


def about_view(request):
    """Display about page."""
    return render(request, 'pages/about.html', {
        'page_title': 'About'
    })
