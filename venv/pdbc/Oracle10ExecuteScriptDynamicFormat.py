import cx_Oracle

try:
    con = cx_Oracle.connect('system/theja2020@localhost:8095/ORCLCDB')
    cursor = con.cursor()
    query = ''
    while True:
        eno = int(input("Enter Employee Number:"))
        eName = input("Enter Employee Name:")
        eSal = float(input("Enter Employee Salary:"))
        eAddr = input("Enter Employee Address:")
        sql = "INSERT INTO employees VALUES({}, '{}', {}, '{}')"
        sql.format(eno, eName, eSal, eAddr)
        query = query + sql.format(eno, eName, eSal, eAddr) + ';'
        option = input("Do you want to insert one more record[Yes|No] :")
        if option == "No":
            print('Firing ', query)
            cursor.executescript(query)
            con.commit()
            print('Done')
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

# Enter Employee Number:400
# Enter Employee Name:400Name
# Enter Employee Salary:4000
# Enter Employee Address:400P
# Do you want to insert one more record[Yes|No] :Yes
# Enter Employee Number:0
# Enter Employee Name:BOSS
# Enter Employee Salary:1
# Enter Employee Address:office
# Do you want to insert one more record[Yes|No] :No
# Firing  INSERT INTO employees VALUES(400, '400Name', 4000.0, '400P');INSERT INTO employees VALUES(0, 'BOSS', 1.0, 'office');
# Traceback (most recent call last):
#   File "/Code/venv/pdbc/Oracle10ExecuteScriptDynamicFormat.py", line <>, in <module>
#     cursor.executescript(query)
# AttributeError: 'cx_Oracle.Cursor' object has no attribute 'executescript'
