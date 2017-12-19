## netstat-parser

Uses netstat to grab the process ID's of listening and established connections. Then checks them against the PID's output by a task list. Where there's a match the task name and PID are output to stdout.

Essentially automates the process of running netstat then cross-referencing  PID's with Task Managers' Details tab. Useful to see at a glance if there are any suspicious programs connected.