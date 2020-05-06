d = eval(input("Enter dictionary:"))
sum = 0
for item in d.items():
    sum += item[1]
print("Sum= ", sum)

# Enter dictionary:{'A':100,'B':200,'C':300}
# Sum=  600
