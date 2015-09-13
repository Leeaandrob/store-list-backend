# coding: utf-8
from fabric.api import *
from fabric import colors
from fabric.contrib import files

env.project = 'storelist'
env.hosts = ['104.236.38.141']
env.user = 'root'
env.repository = "git@github.com:Leeaandrob/store-list-backend.git"


def save_media():
    if files.exists('/home/webapps/storelist/current/media/'):
        run('mv -f /home/webapps/storelist/current/media/ /home/')
        run("mkdir -p /home/webapps/backup_medias/")
        run("cp -r /home/media/ /home/webapps/backup_medias/")
    else:
        run("echo 'Nao tem media'")


def extract_media():
    if files.exists('/home/media/'):
        run("mv /home/media/ /home/webapps/storelist/current/")
    else:
        run('echo "Não existe media.zip"')


def upload_files():
    colors.blue('Enviando arquivos de configuracao prod')
    put('config/deploy_config/id_rsa', '/root/.ssh/')
    put('config/deploy_config/id_rsa.pub', '/root/.ssh/')
    put('config/deploy_config/gunicorn_start.bash', '/home/webapps/')
    put('config/deploy_config/storelist.conf', '/home/webapps/')
    put('config/deploy_config/storelist_supervisor.conf', '/home/webapps/')


def configure_stack():
    run('sudo adduser webapps --home /home/webapps/ --shell /bin/bash/')
    run('sudo adduser webapps sudo')
