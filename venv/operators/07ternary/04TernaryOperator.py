a = int(input("Enter First Number:"))
b = int(input("Enter Second Number:"))
c = int(input("Enter Third Number:"))
max = a if a > b and a > c else b if b > c else c
print("Maximum Value:", max)

# Enter First Number:3
# Enter Second Number:44
# Enter Third Number:5
# Maximum Value: 44
