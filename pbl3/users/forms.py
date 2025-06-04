from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

User = get_user_model()

class UserRegisterForm(UserCreationForm):
    """Form for user registration with email and basic info"""
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class ProfileForm(forms.ModelForm):
    """Form for editing user profile information"""
    class Meta:
        model = Profile
        fields = [
            'profile_picture', 'bio', 'date_of_birth', 'phone_number',
            'address', 'city', 'country', 'postal_code',
            'website', 'github', 'linkedin', 'twitter',
            'email_notifications', 'dark_mode'
        ]
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control'}),
            'website': forms.URLInput(attrs={'class': 'form-control'}),
            'github': forms.URLInput(attrs={'class': 'form-control'}),
            'linkedin': forms.URLInput(attrs={'class': 'form-control'}),
            'twitter': forms.URLInput(attrs={'class': 'form-control'}),
        }
    """Form for editing learning style preferences"""
    
    class Meta:
        model = LearningStyle
        fields = [
            'visual_learner', 'auditory_learner', 'reading_learner', 'kinesthetic_learner',
            'preferred_content_type', 'preferred_session_length', 'learning_pace',
            'preferred_difficulty'
        ]
        widgets = {
            'preferred_content_type': forms.Select(attrs={'class': 'form-control'}),
            'preferred_session_length': forms.Select(attrs={'class': 'form-control'}),
            'learning_pace': forms.Select(attrs={'class': 'form-control'}),
            'preferred_difficulty': forms.Select(attrs={'class': 'form-control'}),
        }
