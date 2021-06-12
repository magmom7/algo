import collections
# list
lst = ['a', 'b', 'c']
lst.extend('d')
print(lst)
'''
결과
['a', 'b', 'c', 'd']
'''
# collections.deque
deq = collections.deque(['a', 'b', 'c'])
deq.extend('d')
print(deq)
'''
결과
deque(['a', 'b', 'c', 'd'])
'''
# 예제3-2. append() vs extend()
lst2 = ['a', 'b', 'c', 'd']
lst2.append('ef')  # append()
lst.extend('ef')  # extend()
print("lst.extend('ef') >> ", lst)
print("lst2.append('ef') >>", lst2)
'''
결과
lst.extend('ef') >> ['a', 'b', 'c', 'd', 'e', 'f']
lst2.append('ef') >> ['a', 'b', 'c', 'd', 'ef']
'''

deq = collections.deque(['a', 'b', 'c'])
deq.extendleft('de')
print(deq)
'''
결과
deque(['e', 'd', 'a', 'b', 'c'])
'''
