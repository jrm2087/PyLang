from distutils.core import setup

try:
    long_description = open('README.md', encoding='utf-8').read()
except (IOError, ImportError):
    long_description = ''
  
setup(
  name = 'traductorPy',
  packages = ['traductorPy'],
  version = '1.3',
  url = 'https://github.com/jrm2087/PyLang',
  description = 'Traductor web',
  long_description = long_description,
  long_description_content_type='text/markdown',
  author = ['José D. Rodríguez','Stiven Perdomo','Juan Camilo Castellanos'],
  author_email = ['jrm2087@gmail.com','stiven97.perdomo@gmail.com ','camilo.castellanos.puentes@gmail.com'],
  keywords = ['traductor','web'],
  python_requires=">=3.6",
  install_requires = ['selenium>=3.141.0'],
  classifiers = [],
)                         