"""
Setup configuration for pytest-start-from plugin
"""
from setuptools import setup

setup(
    name='pytest-start-from',
    version='1.0.0',
    description='A pytest plugin to start test execution from a specific test case',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/pytest-start-from',
    py_modules=['pytest_start_from'],
    install_requires=[
        'pytest>=6.0.0',
    ],
    entry_points={
        'pytest11': [
            'start_from = pytest_start_from',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development :: Testing',
    ],
    python_requires='>=3.7',
    license='MIT',
)
