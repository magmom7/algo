from itertools import permutations
N = int(input())
K = int(input())
data = [input() for _ in range(N)]
res = set([])
for permu in permutations(data, K):
    str = ''
    for i in permu:
        str += i
    res.add(str)
print(len(res))
