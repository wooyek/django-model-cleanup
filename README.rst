====================
Django Model Cleanup
====================


.. image:: https://img.shields.io/pypi/v/django-model-cleanup.svg
        :target: https://pypi.python.org/pypi/django-model-cleanup

.. image:: https://img.shields.io/travis/wooyek/django-model-cleanup.svg
        :target: https://travis-ci.org/wooyek/django-model-cleanup

.. image:: https://readthedocs.org/projects/django-model-cleanup/badge/?version=latest
        :target: https://django-model-cleanup.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status
.. image:: https://coveralls.io/repos/github/wooyek/django-model-cleanup/badge.svg?branch=develop
        :target: https://coveralls.io/github/wooyek/django-model-cleanup?branch=develop
        :alt: Coveralls.io coverage

.. image:: https://codecov.io/gh/wooyek/django-model-cleanup/branch/develop/graph/badge.svg
        :target: https://codecov.io/gh/wooyek/django-model-cleanup
        :alt: CodeCov coverage

.. image:: https://api.codeclimate.com/v1/badges/0e7992f6259bc7fd1a1a/maintainability
        :target: https://codeclimate.com/github/wooyek/django-model-cleanup/maintainability
        :alt: Maintainability

.. image:: https://img.shields.io/github/license/wooyek/django-model-cleanup.svg
        :target: https://github.com/wooyek/django-model-cleanup/blob/develop/LICENSE
        :alt: License

.. image:: https://img.shields.io/twitter/url/https/github.com/wooyek/django-model-cleanup.svg?style=social
        :target: https://twitter.com/intent/tweet?text=Wow:&url=https://github.com/wooyek/django-model-cleanup
        :alt: Tweet about this project

.. image:: https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg
        :target: https://saythanks.io/to/wooyek

Mixins for model cleanup methods and validation error concatenations

* Free software: MIT license
* Documentation: https://django-model-cleanup.readthedocs.io.

Features of CleanMixin
----------------------

* Provides `clean` method implementation
* Call to `full_clean` will result in call to all `clean_*` methods
* All methods will get called regardless of validation errors - get all errors at once
* Auto mapping of errors to field names based on clean method names, if errors have no error_dict

Quickstart
----------

Install Django Model Cleanup::

    pip install django-model-cleanup

Add mixin in your models and enjoy `clean_` method collection and error concatenation when `full_clean` is called:

.. code-block:: python

    from django.core.exceptions import ValidationError
    from django.db import models
    from django.utils.translation import ugettext_lazy as _
    from django_model_cleanup import CleanMixin, ExtensibleValidationError


    class SomeModel(CleanMixin, models.Model):
        lorem = models.CharField(max_length=10, blank=True)

        def clean_foo(self):
            raise ValidationError('Foo is bad')

        def clean_bar(self):
            raise ExtensibleValidationError({'bar': _('Bar is wrong cause %s > %s!')}, code='bar', params=(2, 1))

        def clean_legacy(self):
            # We can't init ValidationError as one-liner, cause dict + params are not compatible
            # We need to wrap a message in ValidationError and put that in dict indicating a field
            msg = _('Bar legacy error %s > %s!')
            error = ValidationError(msg, code='bar', params=(7, 5))
            raise ValidationError({'bar': error})

Each error handling and concatenation is no longer required:

.. code-block:: python

        # This is not longer required:
        def clean(self):
            errors = []
            try:
                self.clean_foo()
            except ValidationError as ex:
                errors.append(ex)
            errors = []
            try:
                self.clean_bar()
            except ValidationError as ex:
                errors.append(ex)
            errors = []
            try:
                self.clean_legacy()
            except ValidationError as ex:
                errors.append(ex)
            if errors:
                raise ValidationError(errors)

Running Tests
-------------

Does the code actually work?

::

    $ pipenv install --dev
    $ pipenv shell
    $ tox


We recommend using pipenv_ but a legacy approach to creating virtualenv and installing requirements should also work.
Please install `requirements/development.txt` to setup virtual env for testing and development.


Credits
-------

This package was created with Cookiecutter_ and the `wooyek/cookiecutter-django-app`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`wooyek/cookiecutter-django-app`: https://github.com/wooyek/cookiecutter-django-app
.. _`pipenv`: https://docs.pipenv.org/install/#fancy-installation-of-pipenv
