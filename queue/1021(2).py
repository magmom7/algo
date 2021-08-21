from sys import stdin
from collections import deque


def pop_left():  
    return stack.popleft()


def move_left():  
    temp = stack.popleft()
    stack.append(temp)
    return


def move_right():  
    temp = stack.pop()
    stack.appendleft(temp)
    return



N, M = map(int, stdin.readline().split())
stack = deque(range(1, N + 1))

num_list = deque()
num_list = list(map(int, stdin.readline().split()))

count = 0
for i in num_list:
    num_index = stack.index(i)
    if i == stack[0]:
        pop_left()
        continue

    if num_index < len(stack) / 2:
        while True:
            if i == stack[0]:
                pop_left()
                break
            move_left()
            count += 1

    else:
        while True:
            if i == stack[0]:
                pop_left()
                break
            move_right()
            count += 1

print(count)
