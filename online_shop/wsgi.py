import os

from django.core.wsgi import get_wsgi_application



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'online_shop.settings')

application = get_wsgi_application()
from accounts.views import create_manager
#creating user with 'manager' role
create_manager()

