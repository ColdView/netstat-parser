'''
Python 3.5.1 Script for Windows which outputs the process id's (PID's) and task names 
of binaries under an established or listening connection state. 
Similar to netstat -aob but without the need for admin privileges.
'''
from subprocess import check_output
import re

def run_cmd(cmd):
    return check_output(cmd, shell=True).decode().split('\r\n')

def get_netstat_pids():
    ns_pids = set()
    for row in run_cmd('netstat -ao'):
        if "LISTENING" not in row and "ESTABLISHED" not in row:
            continue
        pid = row.rsplit(' ', 1)[1]
        if pid not in ns_pids:
            ns_pids.add(pid)
    return ns_pids

def get_tasklist_data():
    pids_tasks = {}
    for row in run_cmd('tasklist')[4:-1]:
        match = re.match(r'(^.+?)\s{2,}(\d+)', row)
        taskname, pid = match.group(1), match.group(2)
        pids_tasks[pid] = taskname
    return pids_tasks

def main():
    pids_tasks = get_tasklist_data()
    ns_pids = get_netstat_pids()
    for pid, taskname in pids_tasks.items():
        if pid in ns_pids:
            print("{:10s} {}".format(pid, taskname))

if __name__ == "__main__":
    main()
