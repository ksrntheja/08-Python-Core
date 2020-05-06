n = int(input("Enter the number of students:"))
d = {}
for i in range(n):
    name = input("Enter Student Name:")
    marks = input("Enter Student Marks:")
    d[name] = marks
print('Student data insertion completed...')
print('*' * 30)
print('NAME', '\t\t', 'MARKS')
print('*' * 30)
for k, v in d.items():
    print(k, '\t\t', v)
print('Search Operation...')
while True:
    name = input("Enter Student Name to get Marks: ")
    marks = d.get(name, -1)
    if marks == -1:
        print("Student Not Found")
    else:
        print("The Marks of", name, "are", marks)
    option = input("Do you want to find another student marks[Yes|No]:")
    if option == "No":
        break
print("Thanks for using our application")

# Enter the number of students:4
# Enter Student Name:AB
# Enter Student Marks:100
# Enter Student Name:C
# Enter Student Marks:150
# Enter Student Name:D
# Enter Student Marks:50
# Enter Student Name:E
# Enter Student Marks:80
# Student data insertion completed...
# ******************************
# NAME 		 MARKS
# ******************************
# AB 		 100
# C 		 150
# D 		 50
# E 		 80
# Search Operation...
# Enter Student Name to get Marks: D
# The Marks of D are 50
# Do you want to find another student marks[Yes|No]:Yes
# Enter Student Name to get Marks: C
# The Marks of C are 150
# Do you want to find another student marks[Yes|No]:No
# Thanks for using our application
