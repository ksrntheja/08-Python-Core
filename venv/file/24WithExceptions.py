try:
    with open("abc  .txt", "w") as f:
        f.write("Hi1\n")
        f.write("Hi2\n")
        print(10 / 0)
        f.write("Hi3\n")
        print("Is File Closed: ", f.closed)
except:
    print("Is File Closed - except: ", f.closed)
print('Done')

# Is File Closed - except:  True
# Done
