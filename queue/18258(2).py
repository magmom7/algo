import sys
from collections import deque

def push(queue, x):
    queue.append(x)
    
def pop(deque):
    return deque.popleft() if deque else -1

def size(queue):
    return len(queue)

def empty(queue):
    return 1 if not queue else 0

def front(queue):
    return queue[0] if queue else -1

def back(queue):
    return queue[-1] if queue else -1

deque = deque()

N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    order = sys.stdin.readline().rstrip().split()
    
    command = order[0]
    
    if(command == "push"):
        push(deque, order[1])
    elif(command == "pop"):
        sys.stdout.write(str(pop(deque)) + "\n")
    elif(command == "size"):
        sys.stdout.write(str(size(deque)) + "\n")
    elif(command == "empty"):
        sys.stdout.write(str(empty(deque)) + "\n")
    elif(command == "front"):
        sys.stdout.write(str(front(deque)) + "\n")
    elif(command == "back"):
        sys.stdout.write(str(back(deque)) + "\n")