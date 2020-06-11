import setuptools

setuptools.setup(
    name='wmclient',
    packages=['wmclient'],
    version='2.0.1-beta12',  # We start with 2.0.0 because it works with new server 2.x.y versions and to be aligned
    # with the other 2.x.y clients
    license='apache-2.0',
    description='WURFL Microservice client for Python',
    long_description="This is the python client for WURFL Microservice. "
                     "WURFL by ScientiaMobile delivers highly accurate device information to enterprises that need to "
                     "augment their business intelligence with a detailed understanding of end-users’ devices: "
                     "Web developers can offer separate user-experience to mobile and web users, or even a completely "
                     "separate experience "
                     "to users of SmartTVs and consoles. "
                     "Ad Tech companies can augment their platforms with device targeting, making their offering more "
                     "compelling for "
                     "advertisers. "
                     "Data Engineers can augment their understanding of their users with several properties related "
                     "to their devices. "
                     "Event Stream platforms can use WURFL for device detection to identify certain classes of errors "
                     "that only happen on specific devices or classes of devices. "
                     "Integrate WURFL Device Detection capabilities into applications to enable use-cases such as: "
                     "mobile optimization, targeted advertising, Event Streams analysis and device analytics (Pro "
                     "Edition). "
                     "With automatic weekly updates of its device library (over 65,000 devices), WURFL delivers fast, "
                     "multi-threaded performance that effectively scales on multi-core processor servers. "
                     "Enterprises can feed WURFL Device Detection into their business intelligence platforms to "
                     "improve understanding of their users, identify trends and problems in their services, "
                     "and plan investments in future strategies based on detailed comprehension of mobile and "
                     "internet-enabled devices.",
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
        'License :: OSI Approved :: Apache Software License',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
