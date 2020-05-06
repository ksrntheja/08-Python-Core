a = int(input("Enter First Number:"))
b = int(input("Enter Second Number:"))
c = int(input("Enter Third Number:"))
min = a if a < b and a < c else b if b < c else c
print("Minimum Value:", min)

# Enter First Number:10
# Enter Second Number:20
# Enter Third Number:1
# Minimum Value: 1
