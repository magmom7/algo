from collections import deque
n, k = map(int, input().split())
data = deque([x for x in range(1, n+1)])

lst = []

while data:
    data.rotate(-k+1)
    lstd = data.popleft()
    lst.append(str(lstd))
print("<%s>" % (", ".join(lst)))
