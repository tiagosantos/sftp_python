#! /usr/bin/python
# -*- coding: utf-8 -*-

import os, paramiko, sys, pickle
from stat import S_ISREG, S_ISDIR
from ConfigParser import RawConfigParser


username = sys.argv[1]
password = sys.argv[2]
arquivo = sys.argv[3]


paramiko.util.log_to_file('./sftp.log')

#acrescente o endereço do servidor abaixo
host = 'www.dominio.com'
port = 22
transport = paramiko.Transport((host, port))


transport.connect(username = username, password = password)

sftp = paramiko.SFTPClient.from_transport(transport)

#acrescente o diretório onde estão os arquivos que serão transferidos
caminho_local = './diretorio_local/'
#acrescente o diretório onde serão transferidos os arquivos
caminho_remoto = './diretorio_remoto/'



filepath = caminho_remoto + arquivo + '.TMP'
#filepathtmp = caminho_remoto + arquivo + tmp
localpath = caminho_local + arquivo

sftp.put(localpath, filepath)
new_filepath = caminho_remoto + arquivo 
sftp.rename(filepath, new_filepath)



sftp.close()
transport.close()
