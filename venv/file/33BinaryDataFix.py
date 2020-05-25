f = open('Hmm.png', 'rb')
data = f.read()
f.close()
print('type(data)', type(data))
f = open('myhmm.png', 'wb')
f.write(data)
f.close()
print('Done')

# type(data) <class 'bytes'>
# Done
