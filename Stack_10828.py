import sys

list = []

def push(data):
    list.append(data)

def pop():
    if len(list) != 0 :
        data = list[-1]
        del list[-1]
        return data
    else :
        return -1
def size():
    data = len(list)
    return data

def empty():
    if len(list) == 0:
        return 1
    else :
        return 0

def top():
    if len(list) == 0:
        return -1
    else :
        return list[-1]

num = int(input())

for i in range(num):

    명령 = sys.stdin.readline().split()

    if 명령[0] == 'push':
        data = push(명령[1])
    elif 명령[0] == 'pop':
        data = pop()
        print(data)
    elif 명령[0] == 'size':
        data = size()
        print(data)
    elif 명령[0] == 'empty':
        data = empty()
        print(data)
    elif 명령[0] == 'top':
        data = top()
        print(data)