cart = [10, 20, 3000, 40, 50]
for item in cart:
    if item >= 500:
        print("We cannot process this order")
        continue
    print(item)
else:
    print("Congrats ...all items processed successfully")

# 10
# 20
# We cannot process this order
# 40
# 50
# Congrats ...all items processed successfully
