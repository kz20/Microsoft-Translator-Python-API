# -*- coding: utf-8 -*-
"""
    The fork of https://github.com/openlabs/Microsoft-Translator-Python-API.
    ====== Original description ========

    Microsoft translator API

    The Microsoft Translator services can be used in web or client
    applications to perform language translation operations. The services
    support users who are not familiar with the default language of a page or
    application, or those desiring to communicate with people of a different
    language group.

    This module implements the AJAX API for the Microsoft Translator service.

    An example::

        >>> from mstranslator import Translator
        >>> translator = Translator('<Your API Key>')
        >>> print translator.translate("Hello", "pt")
        "Olá"

    The documentation for the service can be obtained here:
    http://msdn.microsoft.com/en-us/library/ff512423.aspx

    The project is hosted on GitHub where your could fork the project or report
    issues. Visit https://github.com/openlabs/Microsoft-Translator-Python-API

    :copyright: © 2011 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
import codecs
from setuptools import setup


setup(
    name="mstranslator",
    version="0.1",
    packages=[
        'mstranslator',
    ],
    package_dir={
        'mstranslator': '.'
    },
    author="kz20",
    author_email="brightknopper@gmail.com",
    description="Microsoft Translator - Python API. Fork of https://github.com/kz20/Microsoft-Translator-Python-API.git",
    long_description=codecs.open(
        'README.rst', encoding='UTF-8'
    ).read(),
    license="BSD",
    keywords="translation microsoft",
    url="",
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Internationalization",
        "Topic :: Utilities",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
    ],
    test_suite="mstranslator.test.test_all",
    install_requires=[
        'requests >= 1.2.3',
        'six',
    ]
)
