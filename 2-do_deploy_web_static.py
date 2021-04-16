#!/usr/bin/python3
"""Fabric script"""
from fabric.api import *
import os
env.hosts = ['35.185.2.183', '54.145.7.110']


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
