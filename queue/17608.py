import sys

height = []
N = int(sys.stdin.readline())
n = current_h = before_h = 0

for i in range(N):
    height.append(int(sys.stdin.readline()))
for _ in range(N):
    current_h = height.pop()
    if current_h > before_h:
        n += 1
        before_h = current_h
print(n)
