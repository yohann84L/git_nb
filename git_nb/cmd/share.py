from ..utils import run


def git_pull(silent=False):
    cmd_string = 'git pull'
    run(cmd_string, silent)
