from http.server import executable
import sys
from cx_Freeze import setup, Executable 


base = None
if sys.platform == 'win32':
      base = 'win32GUI'

executables = [
      Executable('OrdenarDatas.py', base=base)
]

#includeFiles=['imagens/']
#packages=['matplotlib']

setup(
      name="OrdenarDatas",
      version="0.0.1",
      author="Cezar Poeta",
      description="Ordenar Datas em uma Lista de Tuplas",
#      options = {'build_exe':{'include_files':includeFiles}},
      executables=executables
)