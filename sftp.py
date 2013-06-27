#! /usr/bin/python
# -*- coding: utf-8 -*-

import os, paramiko, sys, pickle
from stat import S_ISREG, S_ISDIR
from ConfigParser import RawConfigParser

#este bloco recebe os parametros
username = sys.argv[1]
password = sys.argv[2]
host = sys.argv[3]
#acrescente o diretório onde estao os arquivos que serao transferidos
caminho_local = sys.argv[4]
#acrescente o diretório onde serao transferidos os arquivos
caminho_host = sys.argv[5]
arquivo = sys.argv[6]
#cria arquivo de log da conexao sftp
paramiko.util.log_to_file('./sftp.log')

#acrescente o endereço do servidor abaixo
port = 22


#este bloco realiza a conexao

try:
        print '*** Estabelecendo conexao com o servidor: ', host, ' porta: ', port, '...'
        transport = paramiko.Transport((host, port))
        transport.connect(username = username, password = password)
        sftp = paramiko.SFTPClient.from_transport(transport)
        print '*** Conexao realizada'
except:
        print '*** Erro ao se conectar com o servidor: %s: %s' % (e.__class__, e)
        f_log_sftp = open("./sftp.log","r")
        log_sftp = f_log_sftp.read()
        print log_sftp
        sys.exit()

#cria extensao de arquivo temporatio (.TMP)
filepath = caminho_host + arquivo + '.TMP'
localpath = caminho_local + arquivo 
new_filepath = caminho_host + arquivo

#transfere o arquivo
#se precisar fazer download, use get ao invés de put
#exemplo: sftp.get(filepath, localpath)
try:
        sftp.put(localpath, filepath)
except:
        print '*** Erro na tranferencia do arquivo:', arquivo
        f_log_sftp = open("./sftp.log","r")
        log_sftp = f_log_sftp.read()
        print log_sftp
        sys.exit()


#se o arquivo foi transferido corretamente, retira a extensao de temporario
try:
        sftp.rename(filepath, new_filepath)
        print '*** Arquivo ', arquivo,' transferido com sucesso! '
        print '*** Tranferencia finalizada com sucesso!'
except:
        sftp.remove(new_filepath)
        print '*** Arquivo ', arquivo, 'ja existe e sera substituido '
        try:
                sftp.rename(filepath, new_filepath)
                print '*** Tranferencia finalizada com sucesso!'
        except:
                print '*** Erro ao renomear arquivo',arquivo
                sys.exit()


#finaliza conexao
try:
        sftp.close()
        transport.close()
        print '*** Conexao finalizada com sucesso!'
except:
        print '*** Erro ao finalizar conexao!'
        f_log_sftp = open("./sftp.log","r")
        log_sftp = f_log_sftp.read()
        print log_sftp
        sys.exit()

sys.exit()
