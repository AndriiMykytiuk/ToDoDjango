from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

import dj_database_url
DATABASES = {'default': dj_database_url.config(default='postgres://andrii@localhost:5432/todo_data')}