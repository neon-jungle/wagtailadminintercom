import hashlib
import hmac
import json

from django.template import Library
from django.template.loader import render_to_string
from django.utils.html import mark_safe
from django.utils.six import binary_type, text_type
from django.utils.text import force_text

from wagtailadminintercom.conf import settings

register = Library()


def hash_user_value(value):
    print("Hashing", value, type(value), repr(value))
    if not isinstance(value, (text_type, binary_type)):
        value = force_text(value)
    if isinstance(value, text_type):
        value = value.encode('utf-8')
    print("Transformed to", value, type(value), repr(value))

    hash = hmac.new(
        settings.WAGTAILADMIN_INTERCOM_SECRET_KEY.encode('utf-8'),
        value,
        digestmod=hashlib.sha256
    )
    print(hash, hash.hexdigest())
    return hash.hexdigest()


@register.simple_tag(takes_context=True)
def intercom_scripts(context):
    if not settings.WAGTAILADMIN_INTERCOM_ENABLED:
        return ''

    if 'request' not in context:
        return ''

    request = context['request']
    user = request.user
    if not user.is_authenticated():
        return ''
    site = request.site

    identity_style = settings.WAGTAILADMIN_INTERCOM_IDENTITY_VERIFICATION
    email_attr = settings.WAGTAILADMIN_INTERCOM_EMAIL_ATTRIBUTE

    # Basic user information
    intercom_settings = {
        'app_id': settings.WAGTAILADMIN_INTERCOM_APP_ID,
        'name': user.get_full_name(),
        'site_domain': site.hostname,
        'site_name': site.site_name,
    }
    if email_attr:
        intercom_settings['email'] = getattr(user, email_attr)

    # Verify the users identity
    if identity_style is None:
        # Nothing to do if identity verification is not used
        pass
    elif identity_style == 'id':
        # Only set the user_id if the identity style is 'id'.
        intercom_settings.update({
            'user_id': force_text(user.pk),
            'user_hash': hash_user_value(user.pk),
        })
    elif identity_style == 'email':
        # Hash the email and send that through
        intercom_settings.update({
            'user_hash': hash_user_value(intercom_settings['email']),
        })

    return render_to_string('wagtailadminintercom/intercom_scripts.html', {
        'app_id': settings.WAGTAILADMIN_INTERCOM_APP_ID,
        'intercom_settings': mark_safe(json.dumps(intercom_settings, sort_keys=True)),
    })
