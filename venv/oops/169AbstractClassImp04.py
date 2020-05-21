from abc import *


class Test(ABC):

    @abstractmethod
    def m1(self):
        pass


class SubTest(Test):
    pass


st = SubTest()
st.m1()

# Traceback (most recent call last):
#   File "/Code/venv/oops/169AbstractClassImp04.py",", line <>, in <module>
#     st = SubTest()
# TypeError: Can't instantiate abstract class SubTest with abstract methods m1
