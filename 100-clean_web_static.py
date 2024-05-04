#!/usr/bin/python3
"""
Fabric script (based on the file 3-deploy_web_static.py)
that deletes out-of-date archives, using the function
do_clean
"""

import os
from fabric.api import *

env.hosts = ['52.204.70.156', '34.227.91.238']


def do_clean(number=0):
    """Delete out-of-date archives.
    Args:
        number (int): The number of archives to keep.
    If number is 0 or 1, keeps only the most recent archive. If
    number is 2, keeps the most and second-most recent archives,
    etc.
    """
    number = 1 if int(number) == 0 else int(number)

    arc_files = sorted(os.listdir("versions"))
    [arc_files.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in arc_files]

    with cd("/data/web_static/releases"):
        arc_files = run("ls -tr").split()
        arc_files = [a for a in arc_files if "web_static_" in a]
        [arc_files.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in arc_files]
