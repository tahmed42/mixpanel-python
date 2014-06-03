try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='mixpanel-py',
    version='3.1.2.b',
    author='Tareq Ahmed',
    author_email='tahmed57@gmail.com',
    packages=['mixpanel'],
    url='https://github.com/tahmed42/mixpanel-python',
    description='Modified Mixpanel library for Python with import support',
    long_description=open('README.txt').read(),
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2 :: Only',
    ]
)
