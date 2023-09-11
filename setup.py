from setuptools import setup, find_packages

setup(
    name='epss-checker',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'epss-checker=epss_checker.epss_checker:main',
        ],
    },
    author='Omar Santos',
    author_email='santosomar@gmail.com',
    description='A client to query the FIRST EPSS API for CVE EPSS scores',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/santosomar/epss-client',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
