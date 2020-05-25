with open("abc  .txt", "w") as f:
    f.write("Hi1\n")
    f.write("Hi2\n")
    f.write("Hi3\n")
    print("Is File Closed: ", f.closed)

print("Is File Closed: ", f.closed)
