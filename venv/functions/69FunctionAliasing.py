def wish(name):
    print("Good Morning:", name)


greeting = wish
print(id(wish))
print(id(greeting))
greeting('Theja')
wish('Theja')

# 140395298828496
# 140395298828496
# Good Morning: Theja
# Good Morning: Theja
