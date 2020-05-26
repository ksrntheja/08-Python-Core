print("ord('a')", ord('a'))
print("chr(98)", chr(98))
s = input('Enter String:')

output = ''
for ch in s:
    if ch.isalpha():
        x = ch
        output = output + ch
    else:
        d = int(ch)
        newc = chr(ord(x) + d)
        output = output + newc

print(output)

# ord('a') 97
# chr(98) b
# Enter String:a4k3b2
# aeknbd
