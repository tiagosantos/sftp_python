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
host = 'dominio.com'
port = 22


#este bloco realiza a conexão
print 'Estabelecendo conexao com o servidor: ', host, ' porta: ', port, '...'
try:
	transport = paramiko.Transport((host, port))
	transport.connect(username = username, password = password)
	sftp = paramiko.SFTPClient.from_transport(transport)
except:
	print '*** Erro ao se conectar com o servidor: %s: %s' % (e.__class__, e)
    	sys.exit()

#acrescente o diretório onde estão os arquivos que serão transferidos
caminho_local = './arquivos/'
#acrescente o diretório onde serão transferidos os arquivos
caminho_host = './Diretorio/'
#cria extensão de arquivo temporatio (.TMP)
filepath = caminho_host + arquivo + '.TMP'
localpath = caminho_local + arquivo 
new_filepath = caminho_host + arquivo

#transfere o arquivo
#se precisar fazer download, use get ao invés de put
#exemplo: sftp.get(filepath, localpath)
try:
	sftp.put(localpath, filepath)
	print 'Arquivo', arquivo,'tranferido!'
except:
	print '*** Erro na tranferencia do arquivo:', arquivo


#se o arquivo foi transferido corretamente, retira a extensão de temporario
try:
    sftp.rename(filepath, new_filepath)
    print '    Arquivo ', arquivo,' transferido com sucesso! '
except:
	sftp.remove(new_filepath)
	print '*** Erro ao renomear arquivo! O arquivo', arquivo, 'ja existe e sera substituido! ' 
finally:
	sftp.rename(filepath, new_filepath)


#finaliza conexão
try:
	sftp.close()
	transport.close()
	print 'Tranferencia finalizada com sucesso!'
