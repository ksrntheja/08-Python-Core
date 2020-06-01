import cx_Oracle

try:
    con = cx_Oracle.connect('system/theja2020@localhost:8095/ORCLCDB')
    cursor = con.cursor()
    cursor.execute('SELECT * FROM employees')
    with open('AllRec.txt', 'w') as f:
        # f.write(cursor.fetchall())
        #         TypeError: write() argument must be str, not list
        f.write(str(cursor.fetchall()))
except cx_Oracle.DatabaseError as e:
    if con:
        con.rollback()
        print('PROBLEM', e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()

# AllRec.txt
# [(500, 'Name500', 5000.0, '500P'), (600, 'Name600', 6000.0, '600P'), (700, 'Name700', 7000.0, '700P'), (1000, '1000Name', 10000.0, '10P')]
