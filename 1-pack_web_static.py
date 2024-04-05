#!/usr/bin/python3
""" this is a fab script to archive a directory"""
from fabric.api import local
from datetime import datetime

def do_pack():
    """ create a directory and archive"""
    now = datetime.now()
    now_f = now.strftime("%Y%m%d%H%M%S")
    local('mkdir -p versions')
    result = local(f'tar -caf versions/web_static_{now_f}.tgz web_static')
    print(result.failed)
