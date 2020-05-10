print('Even numbers from 1 to 10',
      filter(lambda n: n % 2 == 0, range(1, 11)))

print('Even numbers from 1 to 10',
      list(filter(lambda n: n % 2 == 0, range(1, 11))))

# Even numbers from 1 to 10 <filter object at 0x7f85661dd390>
# Even numbers from 1 to 10 [2, 4, 6, 8, 10]
