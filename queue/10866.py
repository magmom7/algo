import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
stack = deque([])


def push_front(x):
    stack.appendleft(x)


def push_back(x):
    stack.append(x)


def pop_front():
    return stack and stack.popleft() or -1


def pop_back():
    return stack and stack.pop() or -1


def size():
    return len(stack)


def empty():
    return not stack and 1 or 0


def front():
    return stack and stack[0] or -1


def back():
    return stack and stack[-1] or -1


for _ in range(n):
    command = input().split()
    if 'push_front' in command:
        push_front(command[1])
    elif 'push_back' in command:
        push_back(command[1])
    elif 'pop_front' in command:
        print(pop_front())
    elif 'pop_back' in command:
        print(pop_back())
    elif 'size' in command:
        print(size())
    elif 'empty' in command:
        print(empty())
    elif 'front' in command:
        print(front())
    else:
        print(back())
