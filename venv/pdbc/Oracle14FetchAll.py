import cx_Oracle

try:
    con = cx_Oracle.connect('system/theja2020@localhost:8095/ORCLCDB')
    cursor = con.cursor()
    cursor.execute('SELECT * FROM employees')
    rows = cursor.fetchall()
    print('type(rows)', type(rows))
    print('type(rows[0])', type(rows[0]))
    for row in rows:
        print(row)
        print("Employee Number:", row[0])
        print("Employee Name:", row[1])
        print("Employee Salary:", row[2])
        print("Employee Address:", row[3])
        print()
        print()
except cx_Oracle.DatabaseError as e:
    if con:
        con.rollback()
        print('PROBLEM', e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()

# type(rows) <class 'list'>
# type(rows[0]) <class 'tuple'>
# Employee Number: 500
# Employee Name: Name500
# Employee Salary: 5000.0
# Employee Address: 500P
#
#
# (600, 'Name600', 6000.0, '600P')
# Employee Number: 600
# Employee Name: Name600
# Employee Salary: 6000.0
# Employee Address: 600P
#
#
# (700, 'Name700', 7000.0, '700P')
# Employee Number: 700
# Employee Name: Name700
# Employee Salary: 7000.0
# Employee Address: 700P
#
#
# (1000, '1000Name', 10000.0, '10P')
# Employee Number: 1000
# Employee Name: 1000Name
# Employee Salary: 10000.0
# Employee Address: 10P
