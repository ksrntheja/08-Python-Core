city = input("Enter your city Name:")
sCity = city.strip()
if sCity == 'Hyderabad':
    print("Hello Hyderbadi..Adab")
elif sCity == 'Chennai':
    print("Hello Madrasi...Vanakkam")
elif sCity == "Bangalore":
    print("Hello Kannadiga...Shubhodaya")
else:
    print("your entered city is invalid")

# Enter your city Name:Vizag
# your entered city is invalid

# Enter your city Name:Bangalore
# Hello Kannadiga...Shubhodaya

# Enter your city Name:  Bangalore
# Hello Kannadiga...Shubhodaya

# Enter your city Name:   Bangalore
# Hello Kannadiga...Shubhodaya
