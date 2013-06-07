#! /usr/bin/python
# -*- coding: utf-8 -*-

import os, paramiko, sys, pickle
from stat import S_ISREG, S_ISDIR
from ConfigParser import RawConfigParser

#este bloco recebe os parametros
username = sys.argv[1]
password = sys.argv[2]
arquivo = sys.argv[3]

#cria arquivo de log da conexao sftp
paramiko.util.log_to_file('./sftp.log')

#acrescente o endereço do servidor abaixo
host = 'www.dominio.com'
port = 22

#este bloco realiza a conexão
transport = paramiko.Transport((host, port))
transport.connect(username = username, password = password)
sftp = paramiko.SFTPClient.from_transport(transport)

#acrescente o diretório onde estão os arquivos que serão transferidos
caminho_local = './diretorio_local/'
#acrescente o diretório onde serão transferidos os arquivos
caminho_remoto = './diretorio_remoto/'


#cria extensão de arquivo temporatio (.TMP)
filepath = caminho_remoto + arquivo + '.TMP'
#filepathtmp = caminho_remoto + arquivo + tmp
localpath = caminho_local + arquivo

#transfere o arquivo
sftp.put(localpath, filepath)

#se o arquivo foi transferido corretamente, retira a extensão de temporario
new_filepath = caminho_remoto + arquivo 
sftp.rename(filepath, new_filepath)


#finaliza conexão
sftp.close()
transport.close()
