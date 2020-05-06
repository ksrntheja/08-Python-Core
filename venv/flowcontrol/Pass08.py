from abc import *


class Loan(ABC):
    @abstractmethod
    def getInterestRate(self):
        pass


class HomeLoan(Loan):
    def getInterestRate(self):
        return 8


class VehicleLoan(Loan):
    def getInterestRate(self):
        return 11


h = HomeLoan()
print(h.getInterestRate())

v = VehicleLoan()
print(v.getInterestRate())

# 8
# 11