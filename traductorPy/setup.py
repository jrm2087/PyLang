from distutils.core import setup

try:
    description = open('README.md', encoding='utf-8').read()
except (IOError, ImportError):
    description = ''
  
setup(
  name = 'traductorPy',
  packages = ['traductorPy'], # this must be the same as the name above
  version = '1.2.1',
  description = 'Traductor web',
  long_description = description,
  author = ['José D. Rodriguez','Stiven Perdomo', 'Juan Camilo Castellanos'],
  author_email = ['jrm2087@gmail.com','stiven97.perdomo@gmail.com ','camilo.castellanos.puentes@gmail.com'],
  #url = 'https://github.com/jrm2087/traductorPy', # use the URL to the github repo
  #download_url = 'https://github.com/jrm2087/traductorPy/tarball/0.1',
  keywords = ['traductor', 'web'],
  classifiers = [],
  python_requires=">=3.6",
)