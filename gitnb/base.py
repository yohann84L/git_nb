import os
import urllib
from getpass import getpass
from pathlib import Path

from .config import Config
from .utils import run


class Repo(object):
    def __init__(self, username: str, email: str, repo_name: str, path: str = None):
        self.config = Config(username, email, repo_name)
        if path is None:
            path = "/"
        self._path = Path(path)
        os.chdir(self._path)

    def git_clone(self, silent=False):
        pwd = getpass('Password: ')
        pwd = urllib.parse.quote(pwd)  # your password is converted into url format

        cmd_string = 'git clone https://{0}:{1}@github.com/{0}/{2}.git'.format(
            self.config.username,
            pwd,
            self.config.repo_name
        )

        # Execute command
        run(cmd_string, silent)

        # Remove the password from the variable
        cmd_string, password = "", ""

    @staticmethod
    def git_pull(silent=False):
        cmd_string = 'git pull'
        run(cmd_string, silent)
