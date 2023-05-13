#production.pyは本番環境用です。
import dj_database_url

from .base import *


DEBUG = False

try:
    from .local import *
except ImportError:
    pass

# add new for deploy
DATABASES['default'] =  dj_database_url.config()
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# Allow all host headers
ALLOWED_HOSTS = ['*']
