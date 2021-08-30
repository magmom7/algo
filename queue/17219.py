import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dict = {}

for _ in range(N):
    site, ps = input().split()
    dict[site] = ps

for _ in range(M):
    print(dict[input().rstrip()])