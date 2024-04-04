#!/usr/bin/python3
"""Definition of do_pack function"""
from fabric.api import local
from datetime import datetime


def do_pack():
    date = datetime.now().strftime("%Y%m%d%H%M%S")

    try:
        local('mkdir -p versions')
        filename = 'web_static_{}.tgz'.format(date)
        local('tar -cvzf versions/{} web_static'.format(filename))
        return ("versions/{}".format(filename))
    except Exception as e:
        return None


if __name__ == "__main__":
    do_pack()
