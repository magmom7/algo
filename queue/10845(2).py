import sys

n = int(input())
lst = []


def push(x):
    lst.append(x)


def pop():
    if len(lst) == 0:
        print(-1)
    else:
        print(lst.pop(0))


def size():
    print(len(lst))


def empty():
    if len(lst) == 0:
        print(1)
    else:
        print(0)


def front():
    if len(lst) == 0:
        print(-1)
    else:
        print(lst[0])


def back():
    if len(lst) == 0:
        print(-1)
    else:
        print(lst[-1])


for i in range(n):
    a = sys.stdin.readline().strip().split(' ')

    if a[0] == 'push':
        push(a[1])
    elif a[0] == 'pop':
        pop()
    elif a[0] == 'size':
        size()
    elif a[0] == 'empty':
        empty()
    elif a[0] == 'front':
        front()
    elif a[0] == 'back':
        back()
