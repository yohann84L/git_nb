import os


def run(cmd_string: str, silent: bool):
    if silent:
        os.popen(cmd_string).read()
    else:
        print(os.popen(cmd_string).read())
