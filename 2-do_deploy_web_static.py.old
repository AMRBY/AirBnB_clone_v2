#!/usr/bin/python3
""" this is a fab script to archive a directory"""
from fabric.api import env
from fabric.operations import run, put, local
from os.path import exists

env.hosts = ['35.175.129.122', '34.224.16.6']


def do_deploy(archive_path):
    """ create a directory and archive"""

    if not exists(archive_path):
        return False
    try:
        name_tar = local(f'echo {archive_path} \
                | cut -d/ -f2', capture=True)
        name = local(f'echo {name_tar} |cut -d. -f1', capture=True)
        put(f'{archive_path}', "/tmp/")
        run(f'mkdir -p /data/web_static/releases/{name}')
        run(f'tar -xzf /tmp/{name_tar} -C\
                /data/web_static/releases/{name}')
        run(f'rm /tmp/{name_tar}')
        run(f'cp -rp /data/web_static/releases/{name}/web_static/* \
                /data/web_static/releases/{name}')
        run(f'rm -rf /data/web_static/releases/{name}/web_static')
        run(f'rm -rf /data/web_static/current')
        run(f'ln -s /data/web_static/releases/{name} \
                /data/web_static/current')
        print("New version deployed!")
        return True
    except Exception:
        return False
