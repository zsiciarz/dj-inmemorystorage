======================
dj-inmemorystorage
======================

A non-persistent in-memory data storage backend for Django.

Compatible with Django's `storage API <https://docs.djangoproject.com/en/dev/ref/files/storage/>`_.

=====
Usage
=====

In your test settings file, add

.. code:: python

    DEFAULT_FILE_STORAGE = 'inmemorystorage.InMemoryStorage'

===========
Differences
===========

This library is based on `django-inmemorystorage <https://github.com/codysoyland/django-inmemorystorage>`_ by Cody Soyland,
with `modifications <https://github.com/SeanHayes/django-inmemorystorage>`_ made by Seán Hayes with support for the ``url`` method,
with `additional support <https://github.com/Vostopia/django-inmemorystorage>`_ for writing.

Wave's modifications include packaging, and test modifications such that ``python setup.py test`` works. This version
also bumps the version to ``1.0.0`` and renames it to dj-inmemorystorage such that it doesn't conflict on PyPI.
