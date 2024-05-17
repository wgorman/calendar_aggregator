from setuptools import setup, find_packages

setup(
    name='calendar_aggregator',
    version='0.1.0',
    description='An Orlando Calendar Aggregator',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Accelerate Orlando',
    author_email='wgorman@gmail.com',
    url='https://github.com/wgorman/calendar_aggregator',  # Replace with your project's URL
    packages=find_packages(),
    install_requires=[
        'beautifulsoup4>=4.9.3',  # Specify the minimum version you want to support
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Specify your project's Python version compatibility
    include_package_data=True,  # Include package data as specified in MANIFEST.in
)
