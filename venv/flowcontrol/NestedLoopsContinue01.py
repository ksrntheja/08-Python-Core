for i in range(4):
    for j in range(4):
        if i == j:
            continue
        print('i={}, j={}'.format(i, j))
    print()

# i=0, j=1
# i=0, j=2
# i=0, j=3
#
# i=1, j=0
# i=1, j=2
# i=1, j=3
#
# i=2, j=0
# i=2, j=1
# i=2, j=3
#
# i=3, j=0
# i=3, j=1
# i=3, j=2
