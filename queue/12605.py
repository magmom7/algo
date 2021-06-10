n = int(input())

for i in range(n):
    lst = input().split(' ')
    reverse = ' '.join(lst[::-1])
    print(f"Case #{i + 1}: {reverse}")
