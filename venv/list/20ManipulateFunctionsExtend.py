order1 = ["Chicken", "Mutton", "Fish"]
order2 = ["RC", "KF", "FO"]
order1.extend(order2)
print(order1)
print(len(order1))
print(order2)

print()

order1 = ["Chicken", "Mutton", "Fish"]
order2 = ("RC", "KF", "FO")
order1.extend(order2)
print(order1)
print(len(order1))
print(order2)

print()

order1 = ["Chicken", "Mutton", "Fish"]
order2 = ["RC", "KF", "FO"]
order1.append(order2)
print(order1)
print(len(order1))
print(order2)

print()

l1 = [10, 20, 30]
l1.append('ABC')
print(l1)
print(len(l1))

print()

l1 = [10, 20, 30]
l1.extend('ABC')
print(l1)
print(len(l1))

l1 = [10, 20, 30]
print(l1.extend(['ABC']))
print(l1)
print(len(l1))

# ['Chicken', 'Mutton', 'Fish', 'RC', 'KF', 'FO']
# 6
# ['RC', 'KF', 'FO']
#
# ['Chicken', 'Mutton', 'Fish', 'RC', 'KF', 'FO']
# 6
# ('RC', 'KF', 'FO')
#
# ['Chicken', 'Mutton', 'Fish', ['RC', 'KF', 'FO']]
# 4
# ['RC', 'KF', 'FO']
#
# [10, 20, 30, 'ABC']
# 4
#
# [10, 20, 30, 'A', 'B', 'C']
# 6
# None
# [10, 20, 30, 'ABC']
# 4
