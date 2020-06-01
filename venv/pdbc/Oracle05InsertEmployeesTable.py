import cx_Oracle

try:
    con = cx_Oracle.connect('system/theja2020@localhost:8095/ORCLCDB')
    cursor = con.cursor()
    cursor.execute("INSERT INTO employees VALUES(100, 'Theja', 1000, 'BLR')")
    con.commit()
    print('Record Inserted Successfully')
except cx_Oracle.DatabaseError as e:
    if con:
        con.rollback()
        print('PROBLEM', e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()

# Record Inserted Successfully

# [(100, 'Theja', 1000.0, 'BLR')]
