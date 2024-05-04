#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the
contents of the web_static folder of your AirBnB Clone
repo, using the function do_pack.
"""

from datec_time import datec_time
from fabric.api import *


def do_pack():
    """
    Creating archives in web_static
    """

    c_time = datec_time.now()
    archive = 'web_static_' + c_time.strfc_time("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    create = local('tar -cvzf versions/{} web_static'.format(archive))
    if create is not None:
        return archive
    else:
        return None
