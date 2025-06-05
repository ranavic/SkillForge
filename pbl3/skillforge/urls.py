"""
skillforge URL Configuration

This is the main URL configuration for the SkillForge project.
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

from django.views.generic import RedirectView

urlpatterns = [
    # Admin site
    path('admin/', admin.site.urls),
    
    # Home page
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    
    # Dashboard
    path('dashboard/', TemplateView.as_view(template_name='dashboard/dashboard.html'), name='dashboard'),
    
    # Courses
    path('courses/', include('courses.urls', namespace='courses')),
    
    # Users app (authentication and profiles)
    path('accounts/', include('users.urls', namespace='users')),
    
    # AI Tutor app
    path('ai-tutor/', include('ai_tutor.urls', namespace='ai_tutor')),
    
    # Quizzes
    path('quizzes/', include('quizzes.urls', namespace='quizzes')),

    # Convenience redirect for /login/ to /accounts/login/
    path('login/', RedirectView.as_view(url='/accounts/login/', permanent=False)),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Custom error handlers
handler400 = 'skillforge.views.bad_request'
handler403 = 'skillforge.views.permission_denied'
handler404 = 'skillforge.views.page_not_found'
handler500 = 'skillforge.views.server_error'
