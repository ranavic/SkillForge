import os
import sys

# Add the project root (pbl3/) to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skillforge.settings')

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
