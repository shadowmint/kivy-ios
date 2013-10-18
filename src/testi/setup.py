from distutils.core import setup, Extension
from os.path import join
import os

root = os.getcwd()
sources = list(map(lambda x: join(root, 'src', x), [
  'cjunk.c',
  'junk.c'
]))

setup(name='junk',
      version='1.0',
      ext_modules=[Extension('junk', sources)],
      packages=[ 'testi' ]
)
