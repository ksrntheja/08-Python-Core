from abc import *


class CollegeAutomation(ABC):
    @abstractmethod
    def m1(self):
        pass

    @abstractmethod
    def m2(self):
        pass

    @abstractmethod
    def m3(self):
        pass


class AbsCls(CollegeAutomation):
    def m1(self):
        print('m1 method implementation')

    def m2(self):
        print('m2 method implementation')


class ConcreteCls(AbsCls):
    def m3(self):
        print('m3 method implementation')


c = ConcreteCls()
c.m1()
c.m2()
c.m3()

# c = CollegeAutomation()
# Traceback (most recent call last):
#   File "/Code/venv/oops/179ConcreteAbstractInterface.py", line <>, in <module>
#     c = CollegeAutomation()
# TypeError: Can't instantiate abstract class CollegeAutomation with abstract methods m1, m2, m3

# c = AbsCls()
# Traceback (most recent call last):
#   File "/Code/venv/oops/179ConcreteAbstractInterface.py", line <>, in <module>
#     c = AbsCls()
# TypeError: Can't instantiate abstract class AbsCls with abstract methods m3

# m1 method implementation
# m2 method implementation
# m3 method implementation
