====================================
Wagtail admin ↔ Intercom integration
====================================

Add an Intercom widget to your Wagtail admin.

Installing
==========

Install using pip:

.. code-block:: console

    $ pip install wagailadminintercom

Add it to your ``INSTALLED_APPS`` before ``wagtail.wagtailadmin``:

.. code-block:: python

    INSTALLED_APPS = [
        # ...
        'wagailadminintercom',
        'wagtail.wagtailadmin',
        # ...
    ]

Configuring
===========

Add ``WAGTAILADMIN_INTERCOM_APP_ID`` and ``WAGTAILADMIN_INTERCOM_SECRET_KEY`` settings to your settings file:

.. code-block:: python

    WAGTAILADMIN_INTERCOM_APP_ID = 'abc123'
    WAGTAILADMIN_INTERCOM_SECRET_KEY = '983th8fj98hgh98dj09gj08g4w'

By default, identity verification is enabled using user IDs.
This can be overridden using the ``WAGTAILADMIN_INTERCOM_IDENTITY_VERIFICATION`` setting:

.. code-block:: python

    WAGTAILADMIN_INTERCOM_IDENTITY_VERIFICATION = 'email'

This setting can take three possible values:

``'email'``:
    Identity verification using email addresses.
``'id'``:
    Default. Identity verification via user IDs.
``None``:
    Disable identity verification.

The users email address is taken from the ``email`` attribute on the user model by default.
If this is incorrect,
it can be overridden using the ``WAGTAILADMIN_INTERCOM_EMAIL_ATTRIBUTE`` setting.
Set ``WAGTAILADMIN_INTERCOM_EMAIL_ATTRIBUTE`` to ``None`` to disable sending users emails.

By default, the widget will only appear when ``DEBUG is False``
to prevent the widget appearing during development.
To force the widget to show or hide itself,
set the ``WAGTAILADMIN_INTERCOM_ENABLED`` setting:

.. code-block:: python

    WAGTAILADMIN_INTERCOM_ENABLED = True

That is it! You should now see the widget appear in the Wagtail admin.
