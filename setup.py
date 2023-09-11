from setuptools import setup, find_packages

setup(
    name='epss_client',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'epss_client=epss_client.epss_client:main',
        ],
    },
    author='Omar Santos',
    author_email='santosomar@gmail.com',
    description='A client to query the FIRST EPSS API for CVE EPSS scores',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/santosomar/epss_client',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
