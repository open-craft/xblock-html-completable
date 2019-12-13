"""Setup for completable html XBlock."""

import os

from setuptools import setup


def package_data(pkg, roots):
    """Generic function to find package_data.

    All of the files under each of the `roots` will be declared as package
    data for package `pkg`.

    """
    data = []
    for root in roots:
        for dirname, _, files in os.walk(os.path.join(pkg, root)):
            for fname in files:
                data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}


setup(
    name='completable-html-xblock',
    version='0.1.1',
    description='HTML XBlock will help creating and using a secure, easy-to-use and completable HTML blocks',
    license='AGPL v3',
    packages=[
        'completable_html_xblock',
    ],
    install_requires=[
        'XBlock',
        'bleach',
        'html-xblock==0.1.1',
    ],
    entry_points={
        'xblock.v1': [
            'completable_html5 = completable_html_xblock:CompletableHTML5XBlock',
        ]
    },
    package_data=package_data("completable_html_xblock", ["static", "public"]),
)
