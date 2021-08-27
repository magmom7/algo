import sys 
from collections import deque 

n = int(sys.stdin.readline()) 
deque = deque() 

def push(deque, x): 
    deque.append(x) 

def pop(deque):
    if(not deque): 
         return -1 
    else: 
        return deque.popleft() 

def size():
    return len(deque) 

def empty(): 
    if(not deque): 
        return 1 
    else: 
        return 0 

def front(): 
    if(not deque): 
        return -1 
    else: 
        return deque[0]

def back(): 
    if(not deque): 
        return -1 
    else: 
        return deque[-1] 

for i in range(n): 
    oper = sys.stdin.readline().split() 

    if (oper[0] == "push"): 
        push(deque, oper[1]) 
    elif(oper[0] == "pop"): 
        print(pop(deque)) 
    elif(oper[0] == "size"): 
        print(size()) 
    elif(oper[0] == "empty"): 
        print(empty()) 
    elif(oper[0] == "front"): 
        print(front()) 
    elif(oper[0] == "back"): 
        print(back())
