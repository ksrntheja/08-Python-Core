# Sender is responsible to save Employee objects to the file
from PickleMultipleEmp import *
import pickle

f = open('emp.dat', 'wb')
while True:
    eno = int(input('Enter Employee Number:'))
    ename = input('Enter Employee Name:')
    esal = float(input('Enter Employee Salary:'))
    eaddr = input('Enter Employee Address:')
    e = Employee(eno, ename, esal, eaddr)
    pickle.dump(e, f)
    option = input('Do you want to serialize one more Employee object[Yes|No]:')
    if option.lower() == 'no':
        break
print('All Employee objects serialized')

# Enter Employee Number:1
# Enter Employee Name:Theja
# Enter Employee Salary:1
# Enter Employee Address:Theja-Address
# Do you want to serialize one more Employee object[Yes|No]:Yes
# Enter Employee Number:2
# Enter Employee Name:ksrn
# Enter Employee Salary:2
# Enter Employee Address:Ksrn-Address
# Do you want to serialize one more Employee object[Yes|No]:No
# All Employee objects serialized

# emp.dat
# �cPickleMultipleEmp
# Employee
# q )�q}q(X   enoqKX   enameqX   ThejaqX   esalqG?�      X   eaddrqX
#    Theja-Addressqub.�cPickleMultipleEmp
# Employee
# q )�q}q(X   enoqKX   enameqX   ksrnqX   esalqG@       X   eaddrqX   Ksrn-Addressqub.
