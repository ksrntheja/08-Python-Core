from abc import *


class Printer(ABC):
    @abstractmethod
    def printIt(self, text):
        pass

    @abstractmethod
    def disconnect(self):
        pass


class EPSON(Printer):
    def printIt(self, text):
        print('Printing from EPSON Printer...')
        print(text)

    def disconnect(self):
        print('Printing completed on EPSON Printer...')


class HP(Printer):
    def printit(self, text):
        print('Printing from HP Printer...')
        print(text)

    def disconnect(self):
        print('Printing completed on HP Printer...')


with open('config.txt', 'r') as f:
    pname = f.readline()
classname = globals()[pname]
x = classname()
x.printIt('This data has to print...')
x.disconnect()

# Printing from EPSON Printer...
# This data has to print...
# Printing completed on EPSON Printer...
