import os
from barebone import __name__, __version__

from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

setup(
    name=__name__,
    version=__version__,
    packages=find_packages(exclude=['docs', 'tests', 'sandbox']),
    description='Example django app package for setuptools, tox and coverage',
    long_description=README,
    url='https://www.pincoin.info/',
    author='Jonghwa Seo',
    author_email='mairoo' '@' 'pincoin.info',
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    install_requires=[
        'Django',
    ],
    setup_requires=[
    ],
    scripts=[
    ],

    tests_require=[
    ],
    test_suite='runtests.runtests',

    zip_safe=False,
),
