from setuptools import setup

requires = ['Django >= 1.4']
tests_require = requires

setup(
    name="dj-inmemorystorage",
    description="A non-persistent in-memory data storage backend for Django.",
    version="1.0.0",
    url="https://github.com/waveaccounting/django-inmemorystorage",
    license=open('LICENSE').read(),
    long_description=open('README.rst').read(),
    author='Cody Soyland, Seán Hayes, Tore Birkeland, Nick Presta',
    author_email='opensource@waveapps.com',
    packages=[
        'inmemorystorage',
    ],
    zip_safe=True,
    install_requires=requires,
    tests_require=tests_require,
    test_suite='inmemorystorage.storage_tests',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
