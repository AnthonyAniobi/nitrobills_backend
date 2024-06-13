import os
import dj_database_url
from common import *


SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1',]

CSRF_TRUSTED_ORIGINS = ['127.0.0.1',]

DATABASES = {
    'default': dj_database_url.config(
        default= os.getenv("POSTGRESS_DATABASE_URL"),
        conn_max_age=600
    )
}

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = os.getenv("EMAIL")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_PORT = 587
EMAIL_USE_TLS = True
