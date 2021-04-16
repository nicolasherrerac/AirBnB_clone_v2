#!/usr/bin/python3
"""Fabric script"""
from fabric.api import *
from datetime import datetime
import os
env.hosts = ['35.185.2.183', '54.145.7.110']


def do_pack():
    """Create folder and file"""
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    file = "versions/web_static_{}.tgz" .format(time)
    var = local("tar -cvzf {} web_static" .format(file))
    if var.succeeded:
        return file
    else:
        return None


def do_deploy(archive_path):
    """Deploy"""
    if os.path.exists(archive_path) is False:
        return False
    try:
        file = archive_path.split("/")[-1]
        ext = file.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file, path, ext))
        run('rm /tmp/{}'.format(file))
        run('mv {}{}/web_static/* {}{}/'.format(path, ext, path, ext))
        run('rm -rf {}{}/web_static'.format(path, ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, ext))
        return True
    except:
        return False


def deploy():
    """Full deployment"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
