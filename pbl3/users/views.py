from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .forms import UserRegisterForm, ProfileForm
from .models import Profile
from django.contrib.auth.models import User

class ProfileView(View):
    """Class-based view for handling user profiles."""
    @method_decorator(login_required)
    def get(self, request):
        profile = get_object_or_404(Profile, user=request.user)
        form = ProfileForm(instance=profile)
        return render(request, 'users/profile.html', {'form': form, 'profile': profile})
    
    @method_decorator(login_required)
    def post(self, request):
        profile = get_object_or_404(Profile, user=request.user)
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('users_profile')
        return render(request, 'users/profile.html', {'form': form, 'profile': profile})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('users_profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/change_password.html', {'form': form})

def dashboard_view(request):
    """User dashboard view."""
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'dashboard/dashboard.html')

def login_view(request):
    """Handle user login."""
    if request.user.is_authenticated:
        return redirect('dashboard')
        
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                next_url = request.GET.get('next', 'dashboard')
                return redirect(next_url)
        messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    """Handle user logout."""
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('home')

def signup_view(request):
    """Handle new user registration."""
    if request.user.is_authenticated:
        return redirect('dashboard')
        
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create user profile
            Profile.objects.create(user=user)
            # Log the user in
            login(request, user)
            messages.success(request, f'Account created for {user.username}!')
            return redirect('dashboard')
    else:
        form = UserRegisterForm()
    
    return render(request, 'users/signup.html', {'form': form})

def home_view(request):
    """Home page view."""
    return render(request, 'home.html')

def check_username(request):
    """Check if username is available."""
    username = request.GET.get('username', '')
    exists = User.objects.filter(username__iexact=username).exists()
    return JsonResponse({'exists': exists})

def check_email(request):
    """Check if email is available."""
    email = request.GET.get('email', '')
    exists = User.objects.filter(email__iexact=email).exists()
    return JsonResponse({'exists': exists})
