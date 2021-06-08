n = int(input())
cards = list(range(1, n+1))
res = []
while len(cards) > 1:
    res.append(cards[0])
    cards = cards[2:]+[cards[1]]
res.append(cards[0])

print(*res)
