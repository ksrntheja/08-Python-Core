import os

# For cwd
# print(os.listdir('.'))

f = open('mysub1/hi1.txt', 'w')
f.close()
f = open('mysub1/hi2.txt', 'w')
f.close()

f = open('mysub1/mysub2/hello.txt', 'w')
f.close()

print(os.listdir('mysub1'))

print("type(os.walk('mysub1')) ->", type(os.walk('mysub1')))

print()

for element in os.walk('mysub1'):
    print("type(os.walk('element')) ->", type(os.walk('element')))
    print(element)
    print()

# ['hi.txt', 'hi2.txt', 'mysub2', 'hi1.txt']
# type(os.walk('mysub1')) -> <class 'generator'>
#
# type(os.walk('element')) -> <class 'generator'>
# ('mysub1', ['mysub2'], ['hi.txt', 'hi2.txt', 'hi1.txt'])
#
# type(os.walk('element')) -> <class 'generator'>
# ('mysub1/mysub2', ['mysub3'], ['hello.txt'])
#
# type(os.walk('element')) -> <class 'generator'>
# ('mysub1/mysub2/mysub3', [], [])
