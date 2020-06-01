import cx_Oracle

try:
    con = cx_Oracle.connect('system/theja2020@localhost:8095/ORCLCDB')
    cursor = con.cursor()
    sql = "INSERT INTO employees VALUES(:eno, :eno, :esal, :eplace)"
    records = [(500, 'Name500', 5000, '500P'),
               (600, 'Name600', 6000, '600P'),
               (700, 'Name700', 7000, '700P')]
    print('type(records):', type(records))
    print('type(records[0]):', type(records[0]))
    print('type(records[0][1]):', type(records[0][1]))
    cursor.executemany(sql, records)
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

# type(records): <class 'list'>
# type(records[0]): <class 'tuple'>
# type(records[0][1]): <class 'str'>
# Record Inserted Successfully

# DB
# [
#   (100, 'Theja', 1000.0, 'BLR'),
#   (500, 'Name500', 5000.0, '500P'),
#   (600, 'Name600', 6000.0, '600P'),
#   (700, 'Name700', 7000.0, '700P')
# ]
