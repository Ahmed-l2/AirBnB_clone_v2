#!/usr/bin/python3
"""Definition of do_pack function"""
from fabric.api import local
from datetime import datetime


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
