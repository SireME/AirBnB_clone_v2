#!/usr/bin/python3
"""
this modules uses fabric to archive a folder
"""


from fabric.api import *
import datetime as dt


def do_pack():
    """
    do pack method to pack content to tgz
    """

    local("sudo mkdir -p versions")

    date = dt.datetime.now().strftime("%Y%m%d%H%M%S")
    destination_file = f"versions/web_static_{date}.tgz"

    result = local(f"sudo tar -cvzf {destination_file} web_static")
    if result.succeeded:
        return destination_file
    else:
        return None
