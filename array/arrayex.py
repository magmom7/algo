dataset = []
count = 0

dataset = map(list, input("리스트에 넣을 값을 지정하세요 ").split())

a = input("문자를 입력하세요 ")
for v in dataset:
    for index in range(len(v)):
        if v[index] == a:
            count += 1

print(f'{count} 번 나옵니다')
