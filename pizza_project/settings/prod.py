import dj_database_url
import django_heroku
from pizza_project.settings.base import *

DEBUG = False

DATABASE_URL = os.environ.get('DATABASE_URL')
DATABASES['default'] = dj_database_url.config(default=DATABASE_URL, conn_max_age=500, ssl_require=True)

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")

CSRF_TRUSTED_ORIGINS = ['https://*.127.0.0.1', os.environ.get("HOST_NAME")]

django_heroku.settings(locals())
