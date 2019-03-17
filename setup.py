from setuptools import setup
import os

try:
   import pypandoc
   long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
   long_description = open('README.md').read()

setup(name='geograpy2.3',
      version='0.1.0',
      description='Extract countries, regions and cities from a URL or text',
      long_description=long_description,
      url='https://github.com/FloppyDisck/geograpy2',
      download_url ='https://github.com/FloppyDisck/geograpy2',
      author='FloppyDisck',
      author_email='guysebastiangarcia@gmail.com',
      license='MIT',
      packages=['geograpy2'],
      install_requires=[
            'numpy',
            'nltk',
            'newspaper3',
            'jellyfish',
            'pycountry'
      ],
      scripts=['geograpy/bin/geograpy-nltk'],
      package_data = {
            'geograpy': ['data/*.csv'],
      },
      zip_safe=False)