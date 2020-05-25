import pickle


class Employee:
    def __init__(self, eno, ename, esal, eaddr):
        self.eno = eno
        self.ename = ename
        self.esal = esal
        self.eaddr = eaddr

    def display(self):
        print('ENO:{}, ENAME:{}, ESAL:{}, EADDR:{}'.format(self.eno, self.ename, self.esal, self.eaddr))


e = Employee(100, 'Theja', 1000, 'Hyderabad')

with open('emp.dat', 'wb') as f:
    pickle.dump(e, f)
    print('Pickling of Employee object completed')

with open('emp.dat', 'rb') as f:
    obj = pickle.load(f)
    print('Unpickling of Employee object complected')
    print('Printing Employee Information:')
    obj.display()

# Pickling of Employee object completed
# Unpickling of Employee object complected
# Printing Employee Information:
# ENO:100, ENAME:Theja, ESAL:1000, EADDR:Hyderabad

# emp.dat
# �c__main__
# Employee
# q )�q}q(X   enoqKdX   enameqX   ThejaqX   esalqM�X   eaddrqX	   Hyderabadqub.
