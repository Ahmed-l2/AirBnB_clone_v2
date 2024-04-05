#!/usr/bin/python3
"""a Fabric script that generates a .tgz archive"""
from fabric.api import local, env, put, run
from datetime import datetime
import os

env.hosts = ['18.206.233.120', '52.91.146.216']
env.user = 'ubuntu'


def do_pack():
    """generates a .tgz archive from the contents of the web_static"""
    date = datetime.now().strftime("%Y%m%d%H%M%S")

    try:
        local('mkdir -p versions')
        filename = 'web_static_{}.tgz'.format(date)
        local('tar -cvzf versions/{} web_static'.format(filename))
        return ("versions/{}".format(filename))
    except Exception:
        return None


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if not archive_path or not os.path.exists(archive_path):
        return False
    try:
        file_name = os.path.basename(archive_path)
        no_ext = file_name.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_name, path, no_ext))
        run('rm /tmp/{}'.format(file_name))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        print("New version deployed!")
        return True
    except Exception:
        return False
