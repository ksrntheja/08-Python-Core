rec = {}
n = int(input("Enter number of students: "))
i = 1
while i <= n:
    name = input("Enter Student Name: ")
    marks = input("Enter % of Marks of Student: ")
    rec[name] = marks
    i = i + 1
print("Name of Student", "\t", "% of marks")
for x in rec:
    print("\t", x, "\t\t", rec[x])

# Enter number of students: 3
# Enter Student Name: Theja
# Enter % of Marks of Student: 100
# Enter Student Name: Ram
# Enter % of Marks of Student: 80%
# Enter Student Name: Shiva
# Enter % of Marks of Student: 100%
# Name of Student 	 % of marks
# 	 Theja 		 100
# 	 Ram 		 80%
# 	 Shiva 		 100%
