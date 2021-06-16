t = []
for _ in range(int(input())):
    s = input()
    k = 1
    for j in t:
        for i in range(len(s)):
            print(s)
            s = s[1:]+s[0]
            if s == j:
                k = 0
    if k:
        t.append(s)
print(len(t))
