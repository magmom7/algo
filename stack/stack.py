stack_list = list()


def push(data):
    stack_list.append(data)


def pop():
    data = stack_list[-1]
    del stack_list[-1]
    return data


a = int(input("몇번까지 만들까여 "))

for index in range(a):
    push(index)

print(pop())
print(pop())
print(pop())
print(pop())
