'''
Python 3.5.1 Script for Windows which outputs the process id's (PID's) and task names 
of binaries under an established or listening connection state. 
Similar to netstat -aob but without the need for admin privileges.
'''
from subprocess import check_output
import re

def get_netstat_pids():
    pids = []
    netstat_output = check_output("netstat -ao", shell=True).decode()
    for row in netstat_output.split('\r\n'):
        if "LISTENING" in row or "ESTABLISHED" in row:
            pid = row.rsplit(' ', 1)[1]
            if pid not in pids:
                pids.append(pid)
    return(pids)

def get_tasklist_data():
    tasks_pids = []
    tasklist_output = check_output('tasklist', shell=True).decode()
    for row in tasklist_output.split('\r\n')[4:-1]:
        a = re.match(r'^.+?\s{2,}\d+', row).group(0) # Get taskname and pid
        b = re.split(r'\s{2,}', a) # Remove whitespace
        tasks_pids.append(b)
    return(tasks_pids)

def main():
    tasks_pids = get_tasklist_data()
    ns_pids = get_netstat_pids()
    for proc in tasks_pids:
        if proc[1] in ns_pids:
            print("{:30s} {}".format(proc[0], proc[1]))

if __name__ == "__main__":
    main()
