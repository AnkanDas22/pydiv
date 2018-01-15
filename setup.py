from distutils.core import setup

with open('README.md') as f:
    readme=f.read()

with open('LICENSE.txt') as f:
    license=f.read()

setup(
  name = 'pydiv',
  packages = ['pydiv'], # this must be the same as the name above
  version = '1.0',
  description = 'Gives the division forms for decimal numbers',
  author = 'Ankan Das',
  author_email = 'ankandas2222@gmail.com',
  url = 'https://github.com/AnkanDas22/pydiv',
  download_url = 'https://github.com/peterldowns/mypackage/archive/0.1.tar.gz',
  keywords = ['testing', 'logging', 'example'],
  classifiers = [],
)
