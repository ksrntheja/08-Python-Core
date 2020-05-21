from abc import *


class Test(ABC):

    def m1(self):
        print('Non-Abstract method of test class')

    @abstractmethod
    def m2(self):
        pass


class SubTest(Test):

    def m1(self):
        print('Non-Abstract method of test class overriding in SubTest')

    def m2(self):
        print('SubTest - m2 method')


st = SubTest()
st.m1()
st.m2()

# Non-Abstract method of test class overriding in SubTest
# SubTest - m2 method
