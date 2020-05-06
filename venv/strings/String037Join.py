t = ('sunny', 'bunny', 'chinny')
s = '-'.join(t)
print(s)

l = ['hyderabad', 'singapore', 'london', 'dubai']
s = ':'.join(l)
print(s)

s = ' '.join(l)
print(s)

s = ''.join(l)
print(s)

# l = ['05', '01', 2020]
# TypeError: sequence item 2: expected str instance, int found
# l = [5, 1, 2020]
# TypeError: sequence item 0: expected str instance, int found

l = ['05', '01', '2020']
s = '-'.join(l)
print(s)

# sunny-bunny-chinny
# hyderabad:singapore:london:dubai
# hyderabad singapore london dubai
# hyderabadsingaporelondondubai
# 05-01-2020
