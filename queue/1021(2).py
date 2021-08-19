from sys import stdin
from collections import deque


def pop_left():  # 1번 연산
    return stack.popleft()


def move_left():  # 2번 연산
    temp = stack.popleft()
    stack.append(temp)
    return


def move_right():  # 3번 연산
    temp = stack.pop()
    stack.appendleft(temp)
    return


# 큐의 크기 N , 뽑아 내려고 하는 수의 개수 M
# 뽑아내려는 숫자 num
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