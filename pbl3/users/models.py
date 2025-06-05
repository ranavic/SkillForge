from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.utils import timezone

class Profile(models.Model):
    """
    Extended user profile model for SkillForge.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(max_length=20, blank=True)
    
    # Social links
    website = models.URLField(blank=True)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    
    # Preferences
    email_notifications = models.BooleanField(default=True)
    dark_mode = models.BooleanField(default=False)
    
    # Timestamps
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username}'s profile"
    
    @property
    def full_name(self):
        """Return user's full name."""
        return f"{self.user.first_name} {self.user.last_name}".strip() or self.user.username
    
    @property
    def initials(self):
        """Return user's initials."""
        first = self.user.first_name[0] if self.user.first_name else ''
        last = self.user.last_name[0] if self.user.last_name else ''
        return f"{first}{last}".upper() or 'U'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Create a Profile for each new User."""
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """Save the Profile when the User is saved."""
    if hasattr(instance, 'profile'):
        instance.profile.save()
