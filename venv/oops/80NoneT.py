class Test:
    def __init__(self):
        print("Constructor")

    def __del__(self):
        print("Destructor")


t = Test()
print('"t" created')
print('Assigning "None" to t')
t = 'None'
print('Accessing "t"')
print(t)
print("End of application")

# Constructor
# "t" created
# Assigning "None" to t
# Destructor
# Accessing "t"
# None
# End of application
