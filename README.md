sftp com python e paramiko
===========

Sript para transferência de arquivos via sftp com Python utilizando a biblioteca Paramiko.


Python: http://www.python.org/

Paramiko: https://github.com/paramiko/paramiko

Edite a script para se encaixar às suas necessidades.

Para executar, rode:

python usuario senha nome_do_arquivo.txt


Python + Paramiko no Windows


1 - Instalar Python 2.6 no Windows (tive problemas para instalar a biblioteca paramiko em versões mais recentes do Python)
http://www.python.org/download/
Adicionar a Path C:\Python26
  
2 - Instalar módulo PyCrypto (Versão para Windows 32bits e python2.6)
http://www.voidspace.org.uk/python/modules.shtml#pycrypto
  
3 - Instalar packs do GNU (easy install + compiladores)
http://sourceforge.net/projects/mingw/files/Automated%20MinGW%20Installer/mingw-get-inst/mingw-get-inst-20110316/
  
4 - Instalar Paramiko
https://github.com/paramiko/paramiko
Descomprimir e navegar até o diretório via linha de comando
executar:
# python setup.py build --compiler=mingw32 bdist_wininst
# python  setup.py build
# python setup.py install
  
5 - Pronto! ;)
