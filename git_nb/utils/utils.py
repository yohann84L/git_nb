import os
import pathlib
import subprocess
from typing import Union

import requests

from git_nb.config import cfg

T_striter = Union[str, tuple, list]


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


def write_cmd(base_cmd: str, extra: T_striter) -> str:
    #  param check
    if len(base_cmd) == 0:
        raise ValueError(f"Command is null: {base_cmd}")

    if extra is None:
        return base_cmd
    else:
        if isinstance(extra, str):
            return f"{base_cmd} {extra.strip()}"
        else:
            return f"{base_cmd} {' '.join(map(str.strip, extra))}"


def check_folder(path: str) -> pathlib.Path:
    if path is None:
        path = os.getcwd()
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
