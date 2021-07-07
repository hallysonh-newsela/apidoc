from setuptools import setup

setup(
    name='flask_api',
    packages=['app'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)