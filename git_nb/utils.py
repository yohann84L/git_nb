import os
import pathlib

import requests

from .config import cfg


def run(cmd_string: str, silent: bool):
    if silent:
        os.popen(cmd_string).read()
    else:
        print(os.popen(cmd_string).read())


def check_folder(path: str) -> pathlib.Path:
    if path is None:
        path = "/"
    path = pathlib.Path(path)
    if not path.exists():
        print("Folder doesn't exist.")
        path.mkdir(parents=True, exist_ok=True)
        print("Folder created.")

    return path


def is_private() -> bool:
    resp = requests.get(f"https://github.com/{cfg.username}/{cfg.repo_name}.git")
    if resp.status_code != 200:
        return True
    else:
        return False
