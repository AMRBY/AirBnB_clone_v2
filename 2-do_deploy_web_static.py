
#!/usr/bin/python3
"""
Fabric script creates and distributes an archive to your web servers, using the function deploy
"""

from fabric.api import put, run, env
from os.path import exists

env.hosts = ['54.157.183.53', '100.25.145.25']

def do_deploy(archive_path):
    """distributes archive remotely"""
    if exists(archive_path) is False:
        return False
    try:
        fi = archive_path.split("/")[-1]
        na = fi.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, na))
        run('tar -xzf /tmp/{} -C {}{}/'.format(fi, path, na))
        run('rm /tmp/{}'.format(fi))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, na))
        run('rm -rf {}{}/web_static'.format(path, na))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, na))
        return True
    except Exception as e:
        return False
