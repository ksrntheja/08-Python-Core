def calc(a, b):
    sum = a + b
    sub = a - b
    mul = a * b
    div = a / b
    return sum, sub, mul, div


a = 10
b = 20
t = calc(a, b)
print('t =>', t, 'type of t =>', type(t))

# t => (30, -10, 200, 0.5) type of t => <class 'tuple'>
