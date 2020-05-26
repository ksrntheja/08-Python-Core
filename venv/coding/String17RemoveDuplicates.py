s = input('Enter String:')

output = ''
for ch in s:
    if ch not in output:
        output = output + ch
print(output)

print('Using list->')
list = []
for ch in s:
    if ch not in list:
        list.append(ch)
print(''.join(list))

print('Using set->')
set = set(s)
# for ch in s:
#     set.add(ch)
print(''.join(set))

# Enter String:AZZZBCDABBCDABBBBCCCCDDDDEEEEEF
# AZBCDEF
# Using list->
# AZBCDEF
# Using set->
# CABZEFD
