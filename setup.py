from setuptools import setup
import os

try:
   import pypandoc
   long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
   long_description = open('README.md').read()

setup(name='geograpy3',
      version='0.1.0',
      description='Extract countries, regions and cities from a URL or text',
      long_description=long_description,
      url='https://github.com/FloppyDisck/geograpy3',
      download_url ='https://github.com/FloppyDisck/geograpy3',
      author='FloppyDisck',
      author_email='guysebastiangarcia@gmail.com',
      license='MIT',
      packages=['geograpy3'],
      install_requires=[
            'numpy',
            'nltk',
            'newspaper',
            'jellyfish',
            'pycountry'
      ],
      scripts=['geograpy3/bin/geograpy3-nltk'],
      package_data = {
            'geograpy3': ['data/*.csv'],
      },
      zip_safe=False)
