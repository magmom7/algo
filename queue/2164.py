import sys
from collections import deque

n = int(sys.stdin.readline())
d = deque()

for i in range(n):
    d.append(i+1)

while len(d) > 1:
    d.popleft()
    d.append(d.popleft())
print(d.pop())
