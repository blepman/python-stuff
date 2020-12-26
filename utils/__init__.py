from subprocess import check_output


def list_process(proc_name: str):
    """ Check for a running process.
    :arg        proc_name: Name of process e.g "chrome.exe", "dota2.exe", "pycharm64.exe", etc."
    :returns:   List with lists containing process name, and process id (pid)"""
    proc_list = [[i.split()[0], int(i.split()[1])] for i in
                 check_output(["tasklist", "/nh", "/fi", f"IMAGENAME eq {proc_name}"]).decode("cp1252").split("\n")[
                 1:-1]]
    return proc_list if len(proc_list) != 0 else False


# Only semantically different from the above.
list_processes = list_process
