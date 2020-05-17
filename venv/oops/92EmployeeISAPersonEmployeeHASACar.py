class Car:
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color

    def getinfo(self):
        print("\tCar Name:{} \n\t Model:{} \n\t Color:{}".format(self.name, self.model, self.color))


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eatndrink(self):
        print('Eat Biryani and Drink Beer')


class Employee(Person):
    def __init__(self, name, age, eno, esal, car):
        super().__init__(name, age)
        self.eno = eno
        self.esal = esal
        self.car = car

    def work(self):
        print("Coding Python is very easy just like drinking Chilled Beer")

    def empinfo(self):
        print("Employee Name:", self.name)
        print("Employee Age:", self.age)
        print("Employee Number:", self.eno)
        print("Employee Salary:", self.esal)
        self.car.getinfo()


car = Car("Innova", "2.5V", "Grey")
e = Employee('Theja', 50, 500, 5000, car)
e.eatndrink()
e.work()
e.empinfo()

# Eat Biryani and Drink Beer
# Coding Python is very easy just like drinking Chilled Beer
# Employee Name: Theja
# Employee Age: 50
# Employee Number: 500
# Employee Salary: 5000
# 	Car Name:Innova
# 	 Model:2.5V
# 	 Color:Grey
