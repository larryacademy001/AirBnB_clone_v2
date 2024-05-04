#!/usr/bin/python3
"""
 Fabric script (based on the file 1-pack_web_static.py)
 that distributes an archive to your web servers, using
 the function do_deploy
"""

from fabric.api import put, run, env
from os.path import exists
env.hosts = ['52.204.70.156', '34.227.91.238']


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        arc_file_name = archive_path.split("/")[-1]
        no_ext = arc_file_name.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(arc_file_name, path, no_ext))
        run('rm /tmp/{}'.format(arc_file_name))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except:
        return False
