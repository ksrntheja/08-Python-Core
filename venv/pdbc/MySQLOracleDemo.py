import pymysql
import cx_Oracle

try:
    con = pymysql.connect(host='localhost', database='thejadb', user='root', password='theja2020')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM employees")
    data = cursor.fetchall()
    list = []
    for row in data:
        t = (row[0], row[1], row[2], row[3])
        list.append(t)
except pymysql.DatabaseError as e:
    if con:
        con.rollback()
        print("There is a problem with MySql :", e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()

try:
    con = cx_Oracle.connect('system/theja2020@localhost:8095/ORCLCDB')
    cursor = con.cursor()
    sql = "INSERT INTO employees VALUES(:eno,:ename,:esal,:eaddr)"
    cursor.executemany(sql, list)
    con.commit()
    print("Records Copied from MySQL Database to Oracle Database Successfully")
except cx_Oracle.DatabaseError as e:
    if con:
        con.rollback()
        print("There is a problem with sql", e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()

# Records Copied from MySQL Database to Oracle Database Successfully

# ORACLE BEFORE
# type(rows) <class 'list'>
# type(rows[0]) <class 'tuple'>
# (500, 'Name500', 5000.0, '500P')
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


# AFTER
# type(rows) <class 'list'>
# type(rows[0]) <class 'tuple'>
# (500, 'Name500', 5000.0, '500P')
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
# (100, 'MySQL01', 1000.0, 'MySQL01A')
# Employee Number: 100
# Employee Name: MySQL01
# Employee Salary: 1000.0
# Employee Address: MySQL01A
#
#
# (200, 'MySQL02', 2000.0, 'MySQL02A')
# Employee Number: 200
# Employee Name: MySQL02
# Employee Salary: 2000.0
# Employee Address: MySQL02A
#
#
# (300, 'MySQL03', 3000.0, 'MySQL03A')
# Employee Number: 300
# Employee Name: MySQL03
# Employee Salary: 3000.0
# Employee Address: MySQL03A
