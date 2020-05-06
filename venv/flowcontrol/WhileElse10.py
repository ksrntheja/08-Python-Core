cart = [10, 20, 3000, 40, 50]
item = 0
while len(cart) != item:
    if cart[item] >= 500:
        print("We cannot process this order")
        break
    print(cart[item])
    item += 1
else:
    print("Congrats ...all items processed successfully")

# 10
# 20
# We cannot process this order
