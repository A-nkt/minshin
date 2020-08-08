#dev.pyは開発者用です。
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qoutly2mgorejn*)5e+&g=!!*q-yul-@kpv3f&vb5i7jmf54xz'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']

#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

try:
    from .local import *
except ImportError:
    pass
