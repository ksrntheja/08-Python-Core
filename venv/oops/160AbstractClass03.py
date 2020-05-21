from abc import *


class Test(ABC):
    @abstractmethod
    def m1(self):
        pass


t = Test()

# Traceback (most recent call last):
#   File "/Code/venv/oops/160AbstractClass03.py", line <>, in <module>
#     t = Test()
# TypeError: Can't instantiate abstract class Test with abstract methods m1
