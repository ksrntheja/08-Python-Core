import cx_Oracle

try:
    con = cx_Oracle.connect('system/theja2020@localhost:8095/ORCLCDB')
    cursor = con.cursor()
    cursor.execute('DROP TABLE employees')
    print('Table employees dropped')
except cx_Oracle.DatabaseError as e:
    if con:
        con.rollback()
        print('PROBLEM', e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()

# Table employees dropped
