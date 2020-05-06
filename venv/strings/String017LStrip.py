city = input("Enter your city Name:")
lCity = city.lstrip()
if lCity == 'Hyderabad':
    print("Hello Hyderbadi..Adab")
elif lCity == 'Chennai':
    print("Hello Madrasi...Vanakkam")
elif lCity == "Bangalore":
    print("Hello Kannadiga...Shubhodaya")
else:
    print("your entered city is invalid")

# Enter your city Name:Bangalore
# Hello Kannadiga...Shubhodaya

# Enter your city Name:     Bangalore
# Hello Kannadiga...Shubhodaya

# Enter your city Name:Bangalore
# your entered city is invalid
