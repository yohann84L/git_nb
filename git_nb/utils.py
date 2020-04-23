import pathlib
import subprocess

import requests

from .config import cfg


def run(cmd_string: str, silent: bool):
    p = subprocess.Popen(cmd_string, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, )
    stdout = []
    while True:
        line = p.stdout.readline()
        if not isinstance(line, str):
            line = line.decode('utf-8')
        stdout.append(line)
        if not silent:
            print(line)
        if line == '' and p.poll() is not None:
            break


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
