from collections import deque

n = int(input())
cards = deque(list(range(1, n+1)))
res = []
while cards:
    card = cards.popleft()
    res.append(card)
    if cards:
        card = cards.popleft()
        cards.append(card)

print(res)
