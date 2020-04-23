import os
import urllib
from getpass import getpass

from .config import cfg
from .utils import run, check_folder, is_private


def git_init(silent: bool = False):
    cmd_string = 'git init'

    # Execute command
    run(cmd_string, silent)


def git_clone(path: str = None, change_dir: bool = True, silent: bool = False):
    # Check folder
    path = check_folder(path)
    if change_dir:
        os.chdir(path.as_posix())

    # Get password
    if is_private():
        pwd = getpass('Password: ')
        pwd = urllib.parse.quote(pwd)  # your password is converted into url format

        cmd_string = 'git clone https://{0}:{1}@github.com/{0}/{2}.git'.format(
            cfg.username,
            pwd,
            cfg.repo_name
        )
    else:
        cmd_string = 'git clone https://github.com/{0}/{1}'.format(
            cfg.username,
            cfg.repo_name
        )

    # Execute command
    run(cmd_string, silent)

    # Remove the password from the variable
    password = ""


def git_pull(silent=False):
    cmd_string = 'git pull'
    run(cmd_string, silent)
