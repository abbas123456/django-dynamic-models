import os
from setuptools import find_packages, setup

readme_file = os.path.join(os.path.dirname(__file__), 'README.md')
with open(readme_file, 'r') as f:
    long_description = f.read()

setup(
    name='django-dynamic-models-readonly',
    version='0.1.1',
    url='https://github.com/abbas123456/django-dynamic-models-readonly',
    author='Mohammad Abbas',
    author_email='mohammad.abbas86@gmail.com',
    description='Allow dynamic creation and updates to database schema at runtime.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'Django>=2.0',
    ],
    tests_require=[
        'tox',
        'pytest',
        'pytest-django',
        'pytest-cov',
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Framework :: Django'
    ]
)
