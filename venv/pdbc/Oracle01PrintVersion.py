from cx_Oracle import *

con = connect('system/theja2020@localhost:8095/ORCLCDB')
if con is not None:
    print('Connected')
    print(con.version)
    con.close()
else:
    print('Error')

# Connected
# 12.1.0.2.0
