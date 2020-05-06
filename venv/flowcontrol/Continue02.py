cart = [10, 20, 500, 700, 50, 60]
for item in cart:
    if item >= 500:
        print("We cannot process this item :", item)
        continue
    print(item)

# 10
# 20
# We cannot process this item : 500
# We cannot process this item : 700
# 50
# 60
