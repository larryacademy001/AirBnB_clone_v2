#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the
contents of the web_static folder of your AirBnB Clone
repo, using the function do_pack.
"""

from datecur_time import datecur_time
from fabric.api import *


def do_pack():
    """
    Creating archives in web_static
    """

    cur_time = datecur_time.now()
    archive = 'web_static_' + cur_time.strfcur_time("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    create = local('tar -cvzf versions/{} web_static'.format(archive))
    if create is not None:
        return archive
    else:
        return None
