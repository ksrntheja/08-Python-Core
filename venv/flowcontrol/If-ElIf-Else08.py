words_upto_19 = ['', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'TEN',
                 'ELEVEN', 'TWELVE', 'THIRTEEN', 'FOURTEEN', 'FIFTEEN', 'SIXTEEN', 'SEVENTEEN', 'EIGHTEEN', 'NINETEEN']
words_for_tens = ['', '', 'TWENTY', 'THIRTY', 'FORTY', 'FIFTY', 'SIXTY', 'SEVENTY', 'EIGHTY', 'NINETY']

n = int(input("Enter a digit from 0 to 999:"))
if n == 0:
    print('ZERO')
if n < 20:
    print(words_upto_19[n])
elif n < 100:
    q = n // 10
    r = n % 10
    print(words_for_tens[q], words_upto_19[r])
elif n < 1000:
    q_for_hundred = n // 100
    n = n % 100
    q = n // 10
    r = n % 10
    print(words_upto_19[q_for_hundred], 'hundred',
          words_for_tens[q] if n == 0 else 'and ' + words_for_tens[q],
          words_upto_19[r])
else:
    print("PLEASE ENTER A DIGIT FROM 0 TO 999")

# Enter a digit from 0 to 999:0
# ZERO
# Enter a digit from 0 to 999:19
# NINETEEN
# Enter a digit from 0 to 999:20
# TWENTY
# Enter a digit from 0 to 999:80
# EIGHTY
# Enter a digit from 0 to 999:89
# EIGHTY NINE
# Enter a digit from 0 to 999:100
# ONE hundred
# Enter a digit from 0 to 999:800
# EIGHT hundred
# Enter a digit from 0 to 999:888
# EIGHT hundred and EIGHTY EIGHT
# Enter a digit from 0 to 999:999
# NINE hundred and NINETY NINE
# Enter a digit from 0 to 999:1000
# PLEASE ENTER A DIGIT FROM 0 TO 999
