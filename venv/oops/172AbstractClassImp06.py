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

    def m2(self):
        print('SubTest - m2 method')


st = SubTest()
st.m1()
st.m2()

# SubTest - m1 method
# SubTest - m2 method
