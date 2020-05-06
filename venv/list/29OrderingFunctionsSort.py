n = [20, 5, 15, 10, 0]
print(n)
print(n.sort())
print(n)

print()

s = ["Dog", "Banana", "Cat", "Apple"]
print(s)
s.sort()
print(s)

print()

n = [20, 10, "A", "B"]
print(n)
n.sort()
print(n)

# [20, 5, 15, 10, 0]
# None
# [0, 5, 10, 15, 20]
#
# ['Dog', 'Banana', 'Cat', 'Apple']
# ['Apple', 'Banana', 'Cat', 'Dog']
#
# [20, 10, 'A', 'B']
# Traceback (most recent call last):
#   File "/Code/venv/list/29OrderingFunctionsSort.py", line <>, in <module>
#     n.sort()
# TypeError: '<' not supported between instances of 'str' and 'int'
