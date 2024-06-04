import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'online_shop.settings')

import django
django.setup()

application = get_asgi_application()