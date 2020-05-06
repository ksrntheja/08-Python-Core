print()

print("Hello World")
# We can use escape characters also
print("Hello \n World")
print("Hello\tWorld")
# We can use repetetion operator (*) : in the string
print(10 * "Hello")
print("Hello" * 10)
# We can use + operator also : concatenation operator
print("Hello" + "World")
# print("Hello" + 10)
#  Traceback (most recent call last):
#   File "/Code/venv/inputoutputfunctions/03Print.py", line <>, in <module>
#     print("Hello" + 10)
# TypeError: must be str, not int
print("Hello", "World")

a, b, c = 10, 20, 30
print("The Values are :", a, b, c)

print("The Values are :", a, b, c, sep=',')
print("The Values are :", a, b, c, sep=":")
print("The Values are :", a, b, c, sep="hello world")

print("Hello")
print("World")
print("!")

print("Hello", end='')
print("World", end='')
print("!")

print(10, 20, 30, sep=':', end='***')
print(40, 50, 60, sep=':')
print(70, 80, 90, sep='**', end='$$')
print(90, 100)

l = [10, 20, 30, 40]
t = (10, 20, 30, 40)
print(l)
print(t)

name = "Theja"
salary = 10000
gf = "Sunny"
print("Hello {} your salary is {} and Your Friend {} is waiting"
      .format(name, salary, gf))
print("Hello {0} your salary is {1} and Your Friend {2} is waiting"
      .format(name, salary, gf))
print("Hello {2} your salary is {1} and Your Friend {0} is waiting"
      .format(name, salary, gf))
print("Hello {2} your salary is {1} and Your Friend {0} is waiting"
      .format(gf, salary, name))
print("Hello {x} your salary is {y} and Your Friend {z} is waiting"
      .format(x=name, y=salary, z=gf))
print("Hello {x} your salary is {y} and Your Friend {z} is waiting"
      .format(z=gf, y=salary, x=name))
print("Hello {x} your salary is {y} and Your Friend {z} is waiting"
      .format(x=name, y=salary, z=gf), 'Done!')

a, b, c, d = 10, 20, 30, 40
print('a = {}, b = {}, c = {}, d ={}'.format(a, b, c, d))

a, b, c = 10, 20, 30
print('a value is %i' % a)
print('b value is %i and c value is %d' % (b, c))
print('a = %d, b = %d, c = %d' % (a, b, c))

s = "Theja"
list = [10, 20, 30, 40]
print("Hello %s ...The List of Items are %s" % (s, list))

price = 70.56789
print("Price value = {}".format(price))
print("Price value = %f" % price)
print("Price value =     %.2f" % price)

s = "Theja"
a = 48
s1 = "Java"
s2 = "Python"
print("Hello", s, "Your Age is", a)
print("You are teaching", s1, "and", s2)

#
# Hello World
# Hello
#  World
# Hello	World
# HelloHelloHelloHelloHelloHelloHelloHelloHelloHello
# HelloHelloHelloHelloHelloHelloHelloHelloHelloHello
# HelloWorld
# Hello World
# The Values are : 10 20 30
# The Values are :,10,20,30
# The Values are ::10:20:30
# The Values are :hello world10hello world20hello world30
# Hello
# World
# !
# HelloWorld!
# 10:20:30***40:50:60
# 70**80**90$$90 100
# [10, 20, 30, 40]
# (10, 20, 30, 40)
# Hello Theja your salary is 10000 and Your Friend Sunny is waiting
# Hello Theja your salary is 10000 and Your Friend Sunny is waiting
# Hello Sunny your salary is 10000 and Your Friend Theja is waiting
# Hello Theja your salary is 10000 and Your Friend Sunny is waiting
# Hello Theja your salary is 10000 and Your Friend Sunny is waiting
# Hello Theja your salary is 10000 and Your Friend Sunny is waiting
# Hello Theja your salary is 10000 and Your Friend Sunny is waiting Done!
# a = 10, b = 20, c = 30, d =40
# a value is 10
# b value is 20 and c value is 30
# a = 10, b = 20, c = 30
# Hello Theja ...The List of Items are [10, 20, 30, 40]
# Price value = 70.56789
# Price value = 70.567890
# Price value =     70.57
# Hello Theja Your Age is 48
# You are teaching Java and Python
