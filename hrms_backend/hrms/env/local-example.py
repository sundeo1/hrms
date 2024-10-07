from hrms.settings import *
# add local settings in this file 

SECRET_KEY = None

DEBUG = None

ALLOWED_HOSTS = None

# sql lite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# mssql
DATABASES = {
    "default": {
        "ENGINE": "mssql",
        "NAME": "DATABASE_NAME",
        "USER": "USER_NAME",
        "PASSWORD": "PASSWORD",
        "HOST": "HOST_ADDRESS",
        "PORT": "1433",
        "OPTIONS": {"driver": "ODBC Driver 17 for SQL Server",},
    },
}

# mysql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'DATABASE_NAME',
        'USER': 'USER_NAME',
        'PASSWORD': 'PASSWORD',
        'HOST': 'HOST_ADDRESS',
        'PORT': '3306',
    }
}

SMS_BASE_URL = '1gg2kd.api.infobip.com'

SMS_API_KEY = '382cb99fd0aa945329543738061987a7-9d60e8f2-ddb6-4203-88c2-091b28a0674e'