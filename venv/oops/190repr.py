import datetime

today = datetime.datetime.now()
s = repr(today)  # converting datetime object to str
print(s)
d = eval(s)  # converting str object to datetime
print(d)

# datetime.datetime(2020, 5, 21, 20, 45, 50, 187637)
# 2020-05-21 20:45:50.187637
