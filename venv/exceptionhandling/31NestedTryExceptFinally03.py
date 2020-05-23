try:
    print("outer try block")
    print(10 / 0)
    try:
        print("Inner try block")
    except ValueError:
        print("Inner except block")
    finally:
        print("Inner finally block")
except:
    print("outer except block")
finally:
    print("outer finally block")

# outer try block
# outer except block
# outer finally block
