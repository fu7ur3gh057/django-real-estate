from .base import *

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = 'smtp.mailtrap.io'
EMAIL_USE_TLS = True
EMAIL_HOST_USER = '2e6dfd12c3c6ef'
EMAIL_HOST_PASSWORD = '8525a88eefb82a'
EMAIL_PORT = '2525'
DEFAULT_FROM_EMAIL = "info@real-estate.com"
DOMAIN = "localhost:8500"
SITE_NAME = "Real Estate"

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'estate',
#         'USER': 'postgres',
#         'PASSWORD': '12345',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }
