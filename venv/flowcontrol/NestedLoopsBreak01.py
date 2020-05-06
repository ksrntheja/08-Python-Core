for i in range(4):
    for j in range(4):
        if i == j:
            break
        print('i={}, j={}'.format(i, j))
    print()

# i=1, j=0
#
# i=2, j=0
# i=2, j=1
#
# i=3, j=0
# i=3, j=1
# i=3, j=2
