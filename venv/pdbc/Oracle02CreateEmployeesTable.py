import cx_Oracle

try:
    con = cx_Oracle.connect('system/theja2020@localhost:8095/ORCLCDB')
    cursor = con.cursor()
    cursor.execute('CREATE TABLE employees(eNo NUMBER, eName VARCHAR2(10), eSal NUMBER(10, 2), eAddr VARCHAR2(10))')
    print('Table employees created')
except cx_Oracle.DatabaseError as e:
    if con:
        con.rollback()
        print('PROBLEM', e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()

# Table employees created

# PROBLEM ORA-00955: name is already used by an existing object
