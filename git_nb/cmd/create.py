import os
import urllib
from getpass import getpass

from ..config import cfg
from ..utils import run, check_folder, is_private, write_cmd
from ..utils import T_striter


def git_init(path: str = None, extra: T_striter = None, silent: bool = False):
    r"""
    Create an empty Git repository or reinitialize an existing one

    Arguments:
        path (str, optional): Use ``None`` to init a repo in the current
            folder or specified a path to create a new folder.
        extra ([str, list, tuple], optional): Set extra arguments for the
            initialization. Check https://git-scm.com/docs/git-init for more details
        silent (bool, optional): set to ``True`` to hide output of the
            command (default: ``False``).
    """
    # Check folder
    path = check_folder(path)
    os.chdir(path.as_posix())

    # Command
    cmd_string = write_cmd('git init', extra)

    # Execute command
    run(cmd_string, silent)


def git_clone(path: str = None, change_dir: bool = True,
              silent: bool = False):
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
