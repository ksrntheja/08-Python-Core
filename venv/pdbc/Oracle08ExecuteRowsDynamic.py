import cx_Oracle

try:
    con = cx_Oracle.connect('system/theja2020@localhost:8095/ORCLCDB')
    cursor = con.cursor()
    while True:
        eno = int(input("Enter Employee Number:"))
        eName = input("Enter Employee Name:")
        eSal = float(input("Enter Employee Salary:"))
        eAddr = input("Enter Employee Address:")
        sql = "INSERT INTO employees VALUES(%d, '%s', %f, '%s')"
        cursor.execute(sql % (eno, eName, eSal, eAddr))
        con.commit()
        print('Record Inserted Successfully')
        option = input("Do you want to insert one more record[Yes|No] :")
        if option == "No":
            break
except cx_Oracle.DatabaseError as e:
    if con:
        con.rollback()
        print('PROBLEM', e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()

# Enter Employee Number:800
# Enter Employee Name:Name800
# Enter Employee Salary:8
# Enter Employee Address:800P
# Record Inserted Successfully
# Do you want to insert one more record[Yes|No] :Y
# Enter Employee Number:900
# Enter Employee Name:900Name
# Enter Employee Salary:90
# Enter Employee Address:900PP
# Record Inserted Successfully
# Do you want to insert one more record[Yes|No] :N
# Enter Employee Number:1000
# Enter Employee Name:1000Name
# Enter Employee Salary:10000
# Enter Employee Address:10P
# Record Inserted Successfully
# Do you want to insert one more record[Yes|No] :No

# DB
# [
#   (100, 'Theja', 1000.0, 'BLR'),
#   (500, 'Name500', 5000.0, '500P'),
#   (600, 'Name600', 6000.0, '600P'),
#   (700, 'Name700', 7000.0, '700P'),
#   (800, 'Name800', 8.0, '800P'),
#   (900, '900Name', 90.0, '900PP'),
#   (1000, '1000Name', 10000.0, '10P')]
