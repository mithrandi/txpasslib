import versioneer
from setuptools import setup, find_packages

setup(
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    name='txpasslib',
    description='Twisted wrapper for passlib',
    license='Expat',
    url='https://github.com/mithrandi/txpasslib',
    author='Tristan Seligmann',
    author_email='mithrandi@mithrandi.net',
    maintainer='Tristan Seligmann',
    maintainer_email='mithrandi@mithrandi.net',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    zip_safe=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    install_requires=[
        'attrs>=16.0.0',
        'passlib>=1.7.0',
        'Twisted>=15.5.0',
        ],
    extras_require={
        'test': [
            'testtools>=2.2.0',
            'hypothesis>=3.6.0,<4.0.0',
            ],
        },
    )
