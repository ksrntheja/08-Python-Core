import cx_Oracle

try:
    con = cx_Oracle.connect('system/theja2020@localhost:8095/ORCLCDB')
    cursor = con.cursor()
    cursor.execute('SELECT * FROM employees')
    row = cursor.fetchone()
    print('type(row)', type(row))
    while row is not None:
        print(row)
        row = cursor.fetchone()
except cx_Oracle.DatabaseError as e:
    if con:
        con.rollback()
        print('PROBLEM', e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()

# type(row) <class 'tuple'>
# (500, 'Name500', 5000.0, '500P')
# (600, 'Name600', 6000.0, '600P')
# (700, 'Name700', 7000.0, '700P')
# (1000, '1000Name', 10000.0, '10P')
