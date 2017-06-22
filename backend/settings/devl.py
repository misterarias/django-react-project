import os

from .common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'f3u9y@#9zy6=3pctxw6@cap8tx^dcwlc7e2-1+=%39k2i=+o13'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'USER': 'z_admin',
        'PASSWORD': 'z_admin',
        'HOST': '127.0.0.1',
        'NAME': 'zdb',
    }
}

INTERNAL_IPS = ['127.0.0.1']

INSTALLED_APPS += (
    'autofixture',
)

STATICFILES_DIRS.append(
    os.path.join(BASE_DIR, os.pardir, 'frontend', 'build'),
)
