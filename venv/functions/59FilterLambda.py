l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = list(filter(lambda n: n % 2 == 0, l))
print("Even->", even)
odd = list(filter(lambda n: n % 2 != 0, l))
print("Odd->", odd)
divBy3Odd = list(filter(lambda n: n % 2 != 0 and n % 3 == 0, l))
print("divBy3Odd->", divBy3Odd)

numbersInWords = ['One', 'Two', 'Three', 'Four', 'Five']
# numberStartWithT = list(filter(lambda s: s.startswith('T'), numbersInWords))
numberStartWithT = list(filter(lambda s: s[0] == 'T', numbersInWords))
print("numbersInWords->", numberStartWithT)
numberLenDiv3 = list(filter(lambda s: len(s) % 3 == 0, numbersInWords))
print("numberLenDiv3->", numberLenDiv3)

# Even-> [0, 2, 4, 6, 8, 10]
# Odd-> [1, 3, 5, 7, 9]
# divBy3Odd-> [3, 9]
# numbersInWords-> ['Two', 'Three']
# numberLenDiv3-> ['One', 'Two']
