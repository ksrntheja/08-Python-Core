try:
    print("outer try block")
    try:
        print("Inner try block")
        print(10 / 0)
    except ValueError:
        print("Inner except block")
    finally:
        print("Inner finally block")
except:
    print("outer except block")
finally:
    print("outer finally block")

# outer try block
# Inner try block
# Inner finally block
# outer except block
# outer finally block
