import csv

f = open("emp.csv", 'r')
r = csv.reader(f)  # returns csv reader object
print('type(r)', type(r))
data = list(r)
print(data)
for line in data:
    for word in line:
        print(word, "\t", end='')
    print()

# type(r) <class '_csv.reader'>
# [['ENO', 'ENAME', 'ESAL', 'EADDR'], ['1', 'One', '1000', 'One-Address'], ['2', 'Two', '2000', 'Two-Address']]
# ENO 	ENAME 	ESAL 	EADDR
# 1 	One 	1000 	One-Address
# 2 	Two 	2000 	Two-Address
