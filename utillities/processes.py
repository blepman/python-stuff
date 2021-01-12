#!/usr/bin/env python
from platform import system as platform
from subprocess import check_output, DEVNULL, CalledProcessError

platform = platform()


def list_processes(proc_name: str = None):
    """ Check for a running process by name, and list the process ids.
    Works on both windows and linux, hopefully.
    :arg        proc_name: Name of process e.g "chrome.exe", "bash", "pycharm64.exe", etc."
    :returns:   List with process ids """

    if not proc_name:
        return False, "Process name not supplied."

    if not (platform == "Linux" or platform == "Windows"):
        return False, "Platform not supported."

    if platform == "Linux":
        try:
            args = ["pidof", f"{proc_name}"]
            procs = check_output(args, stderr=DEVNULL).decode("utf-8", errors="ignore").split()
            return [i for i in procs] if len(procs) != 0 else False
        except CalledProcessError:
            return False
        except Exception as e:
            return False, e
    else:
        try:
            args = ["tasklist", "/nh", "/fi", f"IMAGENAME eq {proc_name}"]
            procs = [i.split()[1]
                     for i in check_output(args, stderr=DEVNULL).decode("utf-8", errors="ignore").split("\n")[1:-1]]
            return procs if len(procs) != 0 else False
        except CalledProcessError:
            return False
        except Exception as e:
            return False, e
