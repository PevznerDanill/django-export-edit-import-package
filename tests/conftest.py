"""
Pytest configuration for django-export-edit-import tests
"""
import os
import django
from django.conf import settings


def pytest_configure(config):
    """Configure Django settings for testing"""
    if not settings.configured:
        settings.configure(
            DEBUG=True,
            DATABASES={
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': ':memory:',
                }
            },
            INSTALLED_APPS=[
                'django.contrib.auth',
                'django.contrib.contenttypes',
                'django.contrib.sessions',
                'django.contrib.messages',
                'django.contrib.admin',
                'export_edit_import',
                # Add any other required apps here
            ],
            SECRET_KEY='test-secret-key-only-for-testing',
            USE_TZ=True,
            DEFAULT_AUTO_FIELD='django.db.models.BigAutoField',
            # Add media settings for file uploads in tests
            MEDIA_URL='/media/',
            MEDIA_ROOT='/tmp/test_media/',
        )
        django.setup()
