from django.apps import AppConfig
from django.core.checks import Error, register


def check_settings(app_configs, **kwargs):
    from .conf import settings
    # Bail if it is not enabled
    if not settings.WAGTAILADMIN_INTERCOM_ENABLED:
        return
    if settings.WAGTAILADMIN_INTERCOM_APP_ID is None:
        yield Error(
            'WAGTAILADMIN_INTERCOM_APP_ID is not set',
            hint='Log in to Intercom to find you app ID',
            id='wagtailadminintercom.E001',
        )

    id_verification = settings.WAGTAILADMIN_INTERCOM_IDENTITY_VERIFICATION
    if id_verification not in {'id', 'email', None}:
        yield Error(
            'WAGTAILADMIN_INTERCOM_IDENTITY_VERIFICATION has an invalid value',
            hint='Valid values are "email", "id", and None',
            id='wagtailadminintercom.E002',
        )
    if id_verification is not None and settings.WAGTAILADMIN_INTERCOM_SECRET_KEY is None:
        yield Error(
            'WAGTAILADMIN_INTERCOM_SECRET_KEY is not set but identity verification is enabled',
            hint='Log in to Intercom to find you secret key, or disable identity verification',
            id='wagtailadminintercom.E003',
        )
    if id_verification == 'email' and settings.WAGTAILADMIN_INTERCOM_EMAIL_ATTRIBUTE is None:
        yield Error(
            ('WAGTAILADMIN_INTERCOM_EMAIL_ATTRIBUTE is not set but email '
             'identity verification is enabled'),
            hint='Set the email attribute, or disable email identity verification',
            id='wagtailadminintercom.E003',
        )


class WagtailAdminIntercomApp(AppConfig):
    name = 'wagtailadminintercom'

    def ready(self):
        register()(check_settings)
