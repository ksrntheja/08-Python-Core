import queue

# q = queue.PriorityQueue(reverse=True)
# Traceback (most recent call last):
#   File "/Code/venv/multithreading/69PriorityQueue.py", line <>, in <module>
#     q = queue.PriorityQueue(reverse=True)
# TypeError: __init__() got an unexpected keyword argument 'reverse'

print('PriorityQueue with only Numbers')
q = queue.PriorityQueue()
q.put(10)
q.put(5)
q.put(20)
q.put(15)
while not q.empty():
    print(q.get(), end=' ')

print()

print('PriorityQueue with only String')
q = queue.PriorityQueue()
q.put('ball')
q.put('ant')
q.put('Ball')
q.put('Ant')
q.put('20')
q.put('150')
while not q.empty():
    print(q.get(), end=' ')

print()
print()

print('PriorityQueue with only customized String')
q = queue.PriorityQueue()
q.put((1, "AAA"))
q.put((3, "CCC"))
q.put((2, "BBB"))
q.put((4, "DDD"))
while not q.empty():
    print(q.get(), end=' ')
print()
q.put((1, "AAA"))
q.put((3, "CCC"))
q.put((2, "BBB"))
q.put((4, "DDD"))
print('q.get()[1]')
while not q.empty():
    print(q.get()[1], end=' ')

print()
print()

print('PriorityQueue with only customized Number')
q = queue.PriorityQueue()
q.put(1, 10)
q.put(3, 5)
q.put(2, 20)
while not q.empty():
    print(q.get(), end=' ')
print()
q.put(1, 10)
q.put(3, 5)
q.put(2, 20)
# while not q.empty():
#     print(q.get()[1], end=' ')
# Traceback (most recent call last):
#   File "/Code/venv/multithreading/69PriorityQueue.py", line <>, in <module>
#     print(q.get()[1], end=' ')
# TypeError: 'int' object is not subscriptable

# PriorityQueue with only Numbers
# 5 10 15 20
# PriorityQueue with only String
# 150 20 Ant Ball ant ball
#
# PriorityQueue with only customized String
# (1, 'AAA') (2, 'BBB') (3, 'CCC') (4, 'DDD')
# q.get()[1]
# AAA BBB CCC DDD
#
# PriorityQueue with only customized Number
# 1 2 3
