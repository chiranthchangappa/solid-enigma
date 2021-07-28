from setuptools import find_packages, setup

setup(
    name='solid-enigma',
    version=VERSION,
    url='https://github.com/chiranthchangappa/solid-enigma',
    description=(
        "db details selection"),
    long_description=open('README.rst').read(),
    keywords="copy333",
    license='BSD',
    platforms=['windows'],
    #packages=find_packages(exclude=['sandbox*', 'tests*']),
    include_package_data=True,
    install_requires=[
      'sqlalchemy =1.3.17',
      'psycopg2 =2.8.5'
    ],
    #extras_require={
    #    'oscar': ['django-oscar>=2.0,<3.0']
    #},
    # See http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Other/Nonlisted Topic'],
)
