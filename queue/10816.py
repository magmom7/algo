import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
lint_n = list(map(int, input().split()))
m = int(input())
list_m = list(map(int, input().split()))

list = Counter(lint_n)

for k in list_m:
    print(list[k])
