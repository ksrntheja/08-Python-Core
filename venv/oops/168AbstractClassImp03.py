from abc import *


class Test(ABC):

    @abstractmethod
    def m1(self):
        pass


class SubTest(Test):
    pass

#
