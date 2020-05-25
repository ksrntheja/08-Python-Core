data = "All Students are STUPIDS"
f = open("abc.txt", "w")
f.write(data)
with open("abc.txt", "r+") as f:
    text = f.read()
    print(text)
    print("The Current Cursor Position: ", f.tell())
    f.seek(17)
    print("The Current Cursor Position: ", f.tell())
    f.write("GEMS!!!")
    f.seek(0)
    text = f.read()
    print("Data After Modification:")
    print(text)

# All Students are STUPIDS
# The Current Cursor Position:  24
# The Current Cursor Position:  17
# Data After Modification:
# All Students are GEMS!!!
