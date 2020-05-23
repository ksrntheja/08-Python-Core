try:
    print('10/0 ->', 10 / 0)
except (ArithmeticError, ZeroDivisionError) as msg1:
    print('Exception class:', msg1.__class__.__name__)
    print('Plz Provide valid numbers only and problem is:', msg1)
print()
try:
    print('20/0 ->', 20 / 0)
except (ZeroDivisionError, ArithmeticError) as msg2:
    print('Exception class:', msg2.__class__.__name__)
    print('Plz Provide valid numbers only and problem is:', msg2)

# Exception class: ZeroDivisionError
# Plz Provide valid numbers only and problem is: division by zero
#
# Exception class: ZeroDivisionError
# Plz Provide valid numbers only and problem is: division by zero
