from distutils.core import setup

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()
  
setup(
  name = 'traductorPy',
  packages = ['traductorPy', 'traductorPy.plugin'],
  include_package_data=True,
  package_dir={'traductorPy.plugin': 'traductorPy/plugin'},
  package_data={'traductorPy.plugin': ['*']},
  version = '1.5',
  url = 'https://github.com/jrm2087/PyLang',
  description = 'Traductor web',
  long_description = long_description,
  long_description_content_type='text/markdown',
  author = ['José D. Rodríguez','Stiven Perdomo','Juan Camilo Castellanos'],
  author_email = ['jrm2087@gmail.com','stiven97.perdomo@gmail.com ','camilo.castellanos.puentes@gmail.com'],
  keywords = ['traductor','web'],
  python_requires=">=3.6",
  install_requires = ['selenium>=3.141.0', 'bs4>=0.0.1'],
  classifiers = [],
)                         