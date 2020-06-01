import cx_Oracle

try:
    con = cx_Oracle.connect('system/theja2020@localhost:8095/ORCLCDB')
    cursor = con.cursor()
    print('Current Schema:')
    cursor.execute("select sys_context( 'userenv', 'current_schema' ) from dual")
    print(cursor.fetchall())
    print('DESCRIBE employees')
    cursor.execute("SELECT COLUMN_NAME, DATA_TYPE FROM ALL_TAB_COLUMNS WHERE TABLE_NAME='EMPLOYEES' AND OWNER='SYSTEM'")
    print(cursor.fetchall())
except cx_Oracle.DatabaseError as e:
    if con:
        con.rollback()
        print('PROBLEM', e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()

# Current Schema:
# [('SYSTEM',)]
# DESCRIBE employees
# [('ENO', 'NUMBER'), ('ENAME', 'VARCHAR2'), ('ESAL', 'NUMBER'), ('EADDR', 'VARCHAR2')]
