#!/usr/bin/python3
"""
Fabric script that generates a .tgz
archive from the contents of the web_static
folder of your AirBnB Clone repo, using the
function do_pack
"""

from datetime import datetime
from fabric.api import *


def do_pack():
    """making an archive on web_static folder"""

    c_time = datetime.now()
    archive = 'web_static_' + c_time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    create = local('tar -cvzf versions/{} web_static'.format(archive))
    if create is not None:
        return archive
    else:
        return None
