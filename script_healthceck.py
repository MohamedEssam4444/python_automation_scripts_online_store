#!/usr/bin/env python3
import shutil
import psutil
import socket
import report_email
import os
def check_disk_space(disk):
    du=shutil.disk_usage(disk)
    free=(du.free/du.total)*100
    return free>20
def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage <80
def check_cpu_memory():
    mem = psutil.virtual_memory()
    THRESHOLD = 500 * 1024 * 1024 # 500MB
    return mem.available>THRESHOLD
def check_host_resolving():
    localhost_ip=socket.gethostbyname('localhost')
    return localhost_ip == "127.0.0.1"

if not check_cpu_usage():
    print('ERROR!!!!!!!!!')
    message=report_email.generate_withno_attachement('automation@example.com',"{}@example.com".format(os.environ.get('USER')),'Error - CPU usage is over 80%','Please check your system and resolve the issue as soon as possible.')
    report_email.send(message)
elif not check_disk_space("/"):
    print('ERROR!!!!!!!!!')
    message=report_email.generate_withno_attachement('automation@example.com',"{}@example.com".format(os.environ.get('USER')),'Error - Available disk space is less than 20%','Please check your system and resolve the issue as soon as possible.')
    report_email.send(message)

elif not check_cpu_memory():
    print('ERROR cpu memory!')
    message=report_email.generate_withno_attachement('automation@example.com',"{}@example.com".format(os.environ.get('USER')),'Error - Available memory is less than 500MB','Please check your system and resolve the issue as soon as possible.')
    report_email.send(message)

elif not check_host_resolving():
    print('ERROR!!!!!!!!!')
    message=report_email.generate_withno_attachement('automation@example.com',"{}@example.com".format(os.environ.get('USER')),'Error - localhost cannot be resolved to 127.0.0.1','Please check your system and resolve the issue as soon as possible.')
    report_email.send(message)
else: print("everything is OK")
