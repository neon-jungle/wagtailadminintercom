"""
A wrapper around Django settings that has some defaults
"""
from django.conf import settings as django_settings


class SettingsWrapper(object):
    def __init__(self, **extra):
        self.extra = extra

    def __getattr__(self, name):
        try:
            # Check for a user-defined setting first
            return getattr(django_settings, name)
        except AttributeError:
            # No luck, check for a default
            if name in self.extra:
                return self.extra[name]
            # Still no luck! Reraise the AttributeError
            raise


settings = SettingsWrapper(
    # These need to be provided by the developer
    WAGTAILADMIN_INTERCOM_APP_ID=None,
    WAGTAILADMIN_INTERCOM_SECRET_KEY=None,
    # Intercom is enabled if DEBUG is off
    WAGTAILADMIN_INTERCOM_ENABLED=not django_settings.DEBUG,
    # Use ID-based identity verification
    WAGTAILADMIN_INTERCOM_IDENTITY_VERIFICATION='id',
    # Assume the email attribute is in the normal spot
    WAGTAILADMIN_INTERCOM_EMAIL_ATTRIBUTE='email',
)
