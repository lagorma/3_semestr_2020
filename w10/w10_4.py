#!/bin/python
import threading
import time
from queue import Queue
import subprocess


def ping_func(i,queue):
    time.sleep(2)
    host = queue.get()
    print('{}: ping {}'.format(i,host))
    res = subprocess.call("ping -c 1 %s" % host,
                        shell=True,
                        stdout=open('/dev/null', 'w'),
                        stderr=subprocess.STDOUT)
    if res == 0:
        print ("{} работает без ошибок" .format(host))
    else:
        print ("{} не отвечает".format(host))
    queue.task_done()

queue = Queue()
hosts = ['yandex.ru','vk.com','python.org']

for i in range(1,len(hosts)+1):
    a = threading.Thread (target=ping_func, args=(i,queue))
    a.setDaemon(True)
    a.start()

for host in hosts:
    queue.put(host)
queue.join()
