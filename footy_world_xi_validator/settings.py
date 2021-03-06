"""
Django settings for footy_world_xi_validator project.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""
import os

from configurations import Configuration, values

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration


class Common(Configuration):
    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = values.SecretValue()

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = values.BooleanValue(False)

    ALLOWED_HOSTS = values.ListValue([])

    # Application definition
    INSTALLED_APPS = [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        # Static file handler
        "whitenoise.runserver_nostatic",
        "django.contrib.staticfiles",
        # 3rd party
        "django_extensions",
        "debug_toolbar",
        "crispy_forms",
        # Own packages
        "footy_world_xi_validator.users",
        "footy_validator",
    ]

    MIDDLEWARE = [
        "django.middleware.security.SecurityMiddleware",
        "whitenoise.middleware.WhiteNoiseMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
    ]

    ROOT_URLCONF = "footy_world_xi_validator.urls"

    TEMPLATES = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [os.path.join(BASE_DIR, "templates")],
            "APP_DIRS": True,
            "OPTIONS": {
                "context_processors": [
                    "django.template.context_processors.debug",
                    "django.template.context_processors.request",
                    "django.contrib.auth.context_processors.auth",
                    "django.contrib.messages.context_processors.messages",
                ],
            },
        },
    ]

    WSGI_APPLICATION = "footy_world_xi_validator.wsgi.application"

    # Database
    # https://docs.djangoproject.com/en/3.0/ref/settings/#databases
    # DATABASES = {
    #     "default": {
    #         "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
    #         "NAME": os.environ.get(
    #             "SQL_DATABASE", os.path.join(BASE_DIR, "db.sqlite3")
    #         ),
    #         "USER": os.environ.get("SQL_USER", "user"),
    #         "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
    #         "HOST": os.environ.get("SQL_HOST", "localhost"),
    #         "PORT": os.environ.get("SQL_PORT", "5432"),
    #     }
    # }
    DATABASES = values.DatabaseURLValue(
        "sqlite:///{}".format(os.path.join(BASE_DIR, "db.sqlite3"))
    )
    # Password validation
    # https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators
    AUTH_PASSWORD_VALIDATORS = [
        {
            "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
        },
        {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
        {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
        {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
    ]

    # Internationalization
    # https://docs.djangoproject.com/en/3.0/topics/i18n/
    LANGUAGE_CODE = "en-gb"

    TIME_ZONE = "UTC"

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/3.0/howto/static-files/
    STATIC_URL = "/static/"
    STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

    AUTH_USER_MODEL = "users.User"

    # Django Crispy Forms
    CRISPY_TEMPLATE_PACK = "bootstrap4"


class Development(Common):
    """
    The in-development settings and the default configuration.
    """

    DEBUG = True

    ALLOWED_HOSTS = []

    INTERNAL_IPS = ["127.0.0.1"]

    MIDDLEWARE = Common.MIDDLEWARE + ["debug_toolbar.middleware.DebugToolbarMiddleware"]


class Staging(Common):
    """
    The in-staging settings.
    """

    # Security
    SESSION_COOKIE_SECURE = values.BooleanValue(True)
    SECURE_BROWSER_XSS_FILTER = values.BooleanValue(True)
    SECURE_CONTENT_TYPE_NOSNIFF = values.BooleanValue(True)
    SECURE_HSTS_INCLUDE_SUBDOMAINS = values.BooleanValue(True)
    SECURE_HSTS_SECONDS = values.IntegerValue(31536000)
    SECURE_REDIRECT_EXEMPT = values.ListValue([])
    SECURE_SSL_HOST = values.Value(None)
    SECURE_SSL_REDIRECT = values.BooleanValue(True)
    SECURE_PROXY_SSL_HEADER = values.TupleValue(("HTTP_X_FORWARDED_PROTO", "https"))


class Production(Staging):
    """
    The in-production settings.
    """

    if os.getenv("SENTRY_DSN", None):
        sentry_sdk.init(dsn=os.getenv("SENTRY_DSN"), integrations=[DjangoIntegration()])
    Staging.ALLOWED_HOSTS = ["*"]
