import sys

N = int(sys.stdin.readline())
d = {}
for i in range(N):
    n = int(sys.stdin.readline())
    d[n] = d.get(n, 0) + 1
li = sorted(d.items(), key=lambda x:(-x[1], x[0]))

print(li)
print(li[0][0])