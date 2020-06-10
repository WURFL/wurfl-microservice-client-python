from distutils.core import setup

setup(
    name='wurfl-microservice-client-python',
    packages=['wurfl-microservice-client-python'],
    version='2.0.0',  # We start with 2.0.0 because it works with new server 2.x.y versions and to be aligned with the
    # other 2.x.y clients
    license='apache-2.0',
    description='WURFL Microservice (by ScientiaMobile, Inc.) is a mobile device detection service that can quickly '
                'and accurately detect over 500 capabilities of visiting devices. It can differentiate between '
                'portable mobile devices, desktop devices, SmartTVs and any other types of devices that have a web '
                'browser.',
    author='Scientiamobile Inc.',
    author_email='support@scientiamobile.com',
    url='https://github.com/WURFL/wurfl-microservice-client-python',
    download_url='https://github.com/WURFL/wurfl-microservice-client-python/dist/wurfl-microservice-client-python-2.0'
                 '.0.tar.gz',
    keywords=['device', 'mobile', 'device detection', 'analytics'],
    install_requires=[
        'pycurl',
    ],
    classifiers=[
        'Development Status :: 5 - Stable', # We can chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: Apache 2.0 License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
