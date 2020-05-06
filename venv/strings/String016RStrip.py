city = input("Enter your city Name:")
rCity = city.rstrip()
if rCity == 'Hyderabad':
    print("Hello Hyderbadi..Adab")
elif rCity == 'Chennai':
    print("Hello Madrasi...Vanakkam")
elif rCity == "Bangalore":
    print("Hello Kannadiga...Shubhodaya")
else:
    print("your entered city is invalid")

# Enter your city Name:Bangalore
# Hello Kannadiga...Shubhodaya

# Enter your city Name:    Bangalore
# your entered city is invalid

# Enter your city Name:Bangalore
# Hello Kannadiga...Shubhodaya
