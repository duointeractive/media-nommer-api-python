from distutils.core import setup
import media_nommer_api

long_description = open('README.rst').read()

setup(
    name='media-nommer-api',
    version=media_nommer_api.VERSION,
    description='Client library for media-nommer.',
    long_description=long_description,
    author='DUO Interactive, LLC',
    author_email='gtaylor@duointeractive.com',
    license='BSD License',
    url='http://duointeractive.github.com/media-nommer-api-python/',
    platforms=["any"],
    requires=['simplejson'],
    provides=['media_nommer_api'],
    packages=[
        'media_nommer_api',
        'media_nommer_api.presets',
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Environment :: Web Environment',
        'Topic :: Multimedia :: Video :: Conversion',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
