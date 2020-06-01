import pymysql

try:
    con = pymysql.connect(host='localhost', database='thejadb', user='root', password='theja2020')
    cursor = con.cursor()
    cursor.execute(
        'CREATE TABLE employees(eNo int(5) primary key,eName varchar(10),eSal double(10,2),eAddr varchar(10))')
    print("Table Created...")
    sql = "INSERT INTO employees(eNo, eName, eSal, eAddr) VALUES(%s, %s, %s, %s)"
    records = [
        (100, 'MySQL01', 1000, 'MySQL01A'),
        (200, 'MySQL02', 2000, 'MySQL02A'),
        (300, 'MySQL03', 3000, 'MySQL03A')
    ]
    cursor.executemany(sql, records)
    con.commit()
    print("Records Inserted Successfully...")
    cursor.execute("select * from employees")
    data = cursor.fetchall()
    for row in data:
        print("Employee Number:", row[0])
        print("Employee Name:", row[1])
        print("Employee Salary:", row[2])
        print("Employee Address:", row[3])
        print()
    print()

except pymysql.DatabaseError as e:
    if con:
        con.rollback()
        print("There is a problem with sql :", e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()

# /home/ksrntheja/.local/lib/python3.6/site-packages/pymysql/cursors.py:170: Warning: (1681, 'Integer display width is deprecated and will be removed in a future release.')
#   result = self._query(query)
# /home/ksrntheja/.local/lib/python3.6/site-packages/pymysql/cursors.py:170: Warning: (1681, 'Specifying number of digits for floating point data types is deprecated and will be removed in a future release.')
#   result = self._query(query)
# Table Created...
# Records Inserted Successfully...
# Employee Number: 100
# Employee Name: MySQL01
# Employee Salary: 1000.0
# Employee Address: MySQL01A
#
# Employee Number: 200
# Employee Name: MySQL02
# Employee Salary: 2000.0
# Employee Address: MySQL02A
#
# Employee Number: 300
# Employee Name: MySQL03
# Employee Salary: 3000.0
# Employee Address: MySQL03A
