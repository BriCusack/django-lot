# -*- coding: utf-8 -*-
from setuptools import setup
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.settings'

description = """
Django Login over Token.
"""

setup(
    name = "django-lot",
    url = "https://github.com/jespino/django-lot",
    author = "Jesús Espino, Curtis Malone",
    author_email = "jespinog@gmail.com, curtis@tinbrain.net",
    version=':versiontools:lot:',
    packages = [
        "lot",
        "lot.migrations",
    ],
    description = description.strip(),
    install_requires=['django >= 4.2.11', 'simplejson >= 3.19.1'],
    setup_requires = [
        'versiontools >= 1.9.1',
    ],
    zip_safe=False,
    include_package_data = False,
    package_data = {},
    test_suite = 'nose.collector',
    tests_require = ['nose >= 1.3.7', 'django >= 4.2.11'],
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
        "Environment :: Web Environment",
        "Framework :: Django",
    ],
)
