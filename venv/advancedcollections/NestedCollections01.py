listOfTuples = [(10, 20, 30), (40, 50, 60)]
print(listOfTuples)
print("listOfTuples[0][1] ->", listOfTuples[0][1])
print("listOfTuples[1][2] ->", listOfTuples[1][2])

print()

dictOfTuples = {
    'cars': ('A', 'B', 'C'),
    'mobiles': ('P', 'Q', 'R')
}
print(dictOfTuples)
print('Second car -> ', "dictOfTuples['cars'][1] :", dictOfTuples['cars'][1])
print('Second car -> ', "dictOfTuples.get('cars')[1] :", dictOfTuples.get('cars')[1])
print('All mobiles -> ')
# for mobile in dictOfTuples.get('mobiles'):
for mobile in dictOfTuples['mobiles']:
    print(mobile)

# [(10, 20, 30), (40, 50, 60)]
# listOfTuples[0][1] -> 20
# listOfTuples[1][2] -> 60
#
# {'cars': ('A', 'B', 'C'), 'mobiles': ('P', 'Q', 'R')}
# Second car ->  dictOfTuples['cars'][1] : B
# Second car ->  dictOfTuples.get('cars')[1] : B
# All mobiles ->
# P
# Q
# R
