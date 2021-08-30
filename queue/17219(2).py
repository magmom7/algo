N, M = map(int, input().split())
dict = {}

for _ in range(N):
    site, password = map(str, input().split())
    dict[site] = password

for _ in range(M):
    site_address = input()
    print(dict[site_address])