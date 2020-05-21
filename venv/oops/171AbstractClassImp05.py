from abc import *


class Test(ABC):

    @abstractmethod
    def m1(self):
        pass

    @abstractmethod
    def m2(self):
        pass


class SubTest(Test):
    def m1(self):
        print('SubTest - m1 method')


st = SubTest()
st.m1()

# Traceback (most recent call last):
#   File "/Code/venv/oops/167AbstractClassImp02.py", line <>, in <module>
#     st = SubTest()
# TypeError: Can't instantiate abstract class SubTest with abstract methods m2
