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

Features
--------

* Pending :D

Demo
----

To run an example project for this django reusable app, click the button below and start a demo serwer on Heroku

.. image:: https://www.herokucdn.com/deploy/button.png
    :target: https://heroku.com/deploy
    :alt: Deploy Django Opt-out example project to Heroku


Quickstart
----------

Install Django Model Cleanup::

    pip install django-model-cleanup

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_model_cleanup.apps.DjangoModelCleanupConfig',
        ...
    )

Add Django Model Cleanup's URL patterns:

.. code-block:: python

    from django_model_cleanup import urls as django_model_cleanup_urls


    urlpatterns = [
        ...
        url(r'^', include(django_model_cleanup_urls)),
        ...
    ]


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
.. _`pipenv`: https://docs.pipenv.org/install.html#fancy-installation-of-pipenv
