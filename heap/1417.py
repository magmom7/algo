import heapq

N = int(input())
D = int(input())
q = []
for _ in range(N-1):
    n = int(input())
    heapq.heappush(q, -n)
res = 0
while q:
    n = -heapq.heappop(q)
    if D > n:
        break
    D += 1
    res += 1
    heapq.heappush(q, -(n-1))
print(res)
