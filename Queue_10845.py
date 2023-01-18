from sys import stdin

queue_list = []

def push(data):
    queue_list.append(data)

def pop():
    if len(queue_list) != 0:
        print(queue_list[0])
        del queue_list[0]
    else:
        print(-1)

def size():
    print(len(queue_list))

def empty():
    if len(queue_list) != 0:
        print(0)
    else :
        print(1)

def front():
    if len(queue_list) != 0:
        print(queue_list[0])
    else :
        print(-1)

def back():
    if len(queue_list) != 0:
        print(queue_list[-1])
    else :
        print(-1)

def queue_controller(data):
    if data == 'pop':
        pop()
    elif data == 'size':
        size()
    elif data == 'empty':
        empty()
    elif data == 'front':
        front()
    elif data == 'back':
        back()


num = int(stdin.readline())

for i in range(num):
    control = stdin.readline().split()
    if len(control) == 1 :
        queue_controller(control[0])
    elif len(control) == 2 and control[0] == 'push':
        push(int(control[1]))