# Receiver is responsible to deserialize Employee objects
import pickle

f = open('emp.dat', 'rb')
print('Deserializing Employee objects and printing data...')
while True:
    try:
        obj = pickle.load(f)
        obj.display()
    except EOFError:
        print('All Employees Completed')
        break

# Deserializing Employee objects and printing data...
# ENO:1, ENAME:Theja, ESAL:1.0, EADDR:Theja-Address
# ENO:2, ENAME:ksrn, ESAL:2.0, EADDR:Ksrn-Address
# Traceback (most recent call last):
#   File "/Code/venv/serialization/03PickleMultipleReceiver.py", line <>, in <module>
#     obj = pickle.load(f)
# EOFError: Ran out of input

# Deserializing Employee objects and printing data...
# ENO:1, ENAME:Theja, ESAL:1.0, EADDR:Theja-Address
# ENO:2, ENAME:ksrn, ESAL:2.0, EADDR:Ksrn-Address
# All Employees Completed
