from setuptools import setup

setup(
    name="bzt-s3-reader",
    version="0.0.0",
    author="Cezary Kujawski",
    author_email="cezkuj@gmail.com",
    license="Apache License 2.0",
    description="Python module for Taurus to access files in S3",
    url='https://github.com/cezkuj/bzt-s3-reader',
    keywords=[],
    packages=["bzts3reader"],
    install_requires=[
        'bzt',
        'boto3'
    ],
    include_package_data=True,
)
