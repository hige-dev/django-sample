from ..base.default import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.postgresql',
         'NAME': 'mydatabase',
         'USER': 'djangouser',
         'PASSWORD': 'djangopassword',
         'HOST': 'localhost',
         'PORT': '5432',
     }
 }
