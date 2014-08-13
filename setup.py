import sys
import xplat
from setuptools import setup, find_packages

''' 
packaging modeled after 
https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty/
'''

def read(filename):
    return open(filename).read()

setup(
    name='xplat',
    version=xplat.__version__,
    description='Cross Platform Function Library',
    long_description=(read('README.rst')),
    url='http://github.com/dopry/python-xplat',
    author='Darrel O\'Pry',
    author_email='darrel.opry@gmail.com',
    packages=['xplat'],
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    license=read('LICENSE'),
)
