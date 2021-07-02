def hash_func(key):
    return key % 5


data1 = 'Andy'
data2 = 'Dave'
data3 = 'Trump'
data4 = 'Anthor'

print(ord(data1[0]), ord(data2[0]), ord(data3[0]))
print(ord(data1[0]), hash_func(ord(data1[0])))
print(ord(data1[0]), ord(data4[0]))
