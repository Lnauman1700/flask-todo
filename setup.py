from setuptools import find_packages, setup

setup(
    name='flask_todo',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'psycopg2'
    ],
    extras_require={
        'test': ['pytest', 'coverage']
    },
)
