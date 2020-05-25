import csv

with open("emp.csv", "w") as f:
    w = csv.writer(f)  # returns csv writer object
    print('type(w):', type(w))
    w.writerow(["ENO", "ENAME", "ESAL", "EADDR"])
    n = int(input("Enter Number of Employees:"))
    for i in range(n):
        eno = input("Enter Employee No:")
        ename = input("Enter Employee Name:")
        esal = input("Enter Employee Salary:")
        eaddr = input("Enter Employee Address:")
        w.writerow([eno, ename, esal, eaddr])
print("Total Employees data written to csv file successfully")

# type(w): <class '_csv.writer'>
# Enter Number of Employees:2
# Enter Employee No:1
# Enter Employee Name:One
# Enter Employee Salary:1000
# Enter Employee Address:One-Address
# Enter Employee No:2
# Enter Employee Name:Two
# Enter Employee Salary:2000
# Enter Employee Address:Two-Address
# Total Employees data written to csv file successfully
