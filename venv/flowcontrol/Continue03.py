# print(100 / 0)
# print(100 // 0)
numbers = [10, 20, 0, 5, 0, 30]
for n in numbers:
    if n == 0:
        print("Hey how we can divide with zero..just skipping")
        continue
    print("100/{} = {}".format(n, 100 / n))

# 100/10 = 10.0
# 100/20 = 5.0
# Hey how we can divide with zero..just skipping
# 100/5 = 20.0
# Hey how we can divide with zero..just skipping
# 100/30 = 3.3333333333333335
