#!/usr/bin/python3
"""a Fabric script that generates a .tgz archive"""
from fabric.api import local, env, put, run, lcd, cd
from datetime import datetime
import os

env.hosts = ['52.3.255.136', '54.144.142.157']
env.user = 'ubuntu'


def do_pack():
    """generates a .tgz archive from the contents of the web_static"""
    date = datetime.now().strftime("%Y%m%d%H%M%S")

    try:
        local('mkdir -p versions')
        filename = 'versions/web_static_{}.tgz'.format(date)
        local('tar -cvzf {} web_static'.format(filename))
        return filename
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


def deploy():
    """Deploy the the archive"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)


def do_clean(number=0):
    """Deletes out-of-date archives"""
    if int(number) == 0:
        number = 1
    else:
        number = int(number)

    files = sorted(os.listdir("versions"))

    for i in range(number):
        files.pop()

    with lcd("versions"):
        for file in files:
            local("rm ./{}".format(file))

    with cd("/data/web_static/releases"):
        files = run("ls -tr").split()
        for file in files:
            if "web_static_" in file:
                files.append(file)

        for i in range(number):
            files.pop()

        for file in files:
            run("rm -rf ./{}".format(file))
