queue_list = list()


def enqueue(data):
    queue_list.append(data)


def dequeue():
    data = queue_list[0]
    del queue_list[0]
    return data


a = int(input("몇번까지 만들까여 "))
for index in range(a):
    enqueue(index)

print("FIFO")
print(dequeue())
print(dequeue())
print(dequeue())
