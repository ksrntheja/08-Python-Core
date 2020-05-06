list = []
print(list.append("A"))
list.append("B")
list.append("C")
print(list)

list = []
for i in range(101):
    if i % 10 == 0:
        list.append(i)
print(list)

# None
# ['A', 'B', 'C']
# [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
