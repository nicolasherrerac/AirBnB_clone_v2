#!/usr/bin/env bash
"""script that generates a .tgz"""
from datetime import datetime
from fabric.api import local 

def do_pack():
    """Create folder and file"""
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    local ("mkdir -p versions")
    file = "versions/web_static_{}.tgz" .format(time)
    var = local("tar -cvzf {} web_static" .format(file))
    if var.succeeded:
        return file
    else:
        return None
