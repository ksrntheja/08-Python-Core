import cx_Oracle

try:
    con = cx_Oracle.connect('system/theja2020@localhost:8095/ORCLCDB')
    cursor = con.cursor()
    cutOffSalary = float(input("Enter CutOff Salary:"))
    sql = 'DELETE FROM employees WHERE eSal < %f'
    cursor.execute(sql % cutOffSalary)
    con.commit()
    print("Records Deleted Successfully")
except cx_Oracle.DatabaseError as e:
    if con:
        con.rollback()
        print('PROBLEM', e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()

# DB Before
# [
#   (100, 'Theja', 1050.0, 'BLR'),
#   (500, 'Name500', 5000.0, '500P'),
#   (600, 'Name600', 6000.0, '600P'),
#   (700, 'Name700', 7000.0, '700P'),
#   (800, 'Name800', 58.0, '800P'),
#   (900, '900Name', 140.0, '900PP'),
#   (1000, '1000Name', 10000.0, '10P'),
#   (200, '200Name', 2050.0, '200P'),
#   (300, '300Name', 3050.0, '300P')]

# Enter CutOff Salary:5000
# Records Deleted Successfully

# DB After
# [
#   (500, 'Name500', 5000.0, '500P'),
#   (600, 'Name600', 6000.0, '600P'),
#   (700, 'Name700', 7000.0, '700P'),
#   (1000, '1000Name', 10000.0, '10P')]
