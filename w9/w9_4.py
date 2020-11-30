#!/bin/python
class Terminate(Exception):
   pass

class Connection(Exception):
    pass

def connect_user(username):
    with open('message.txt','w') as f:
        yield from write_to_file(f)

def write_to_file(f_obj):
    while True:
        try:
            x = yield
            f_obj.writelines(x)
            f_obj.writelines('\n')
        except Terminate:
            break
    f_obj.close()

def task_planner():
    users = []
    while True:
        try:
            username = yield
            users.append(username)
        except Connection:
            yield from connect_user(users)


coroutine = task_planner()
next(coroutine)
coroutine.send('name1')
coroutine.send('name2')
coroutine.throw(Connection)
coroutine.send('sms1')
coroutine.send('sms2')
coroutine.throw(Terminate)
coroutine.close()
