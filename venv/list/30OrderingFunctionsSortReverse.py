n = [20, 5, 15, 10, 0]
print(n)
n.sort(reverse=True)
print('Reverse=True', n)
n.sort(reverse=False)
print('Reverse=False', n)

print()

s = ["Dog", "Banana", "Cat", "Apple"]
print(s)
s.sort(reverse=True)
print('Reverse=True', s)
s.sort(reverse=False)
print('Reverse=False', s)

# [20, 5, 15, 10, 0]
# Reverse=True [20, 15, 10, 5, 0]
# Reverse=False [0, 5, 10, 15, 20]
#
# ['Dog', 'Banana', 'Cat', 'Apple']
# Reverse=True ['Dog', 'Cat', 'Banana', 'Apple']
# Reverse=False ['Apple', 'Banana', 'Cat', 'Dog']
