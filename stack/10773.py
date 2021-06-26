n = int(input())
b = []
for i in range(n):
    num = int(input())
    if num == 0:
        b.pop()
    else:
        b.append(num)
print(sum(b))
