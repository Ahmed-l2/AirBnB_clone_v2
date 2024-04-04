#!/usr/bin/python3
"""Definition of do_pack function"""
from fabric.api import local
from datetime import datetime

def do_pack():
    date = datetime.now().strftime("%Y%m%d%H%M%S")

    local('tar -cvzf versions/web_static_{}.tgz web_static'.format(date))


if __name__ == "__main__":
    do_pack()
