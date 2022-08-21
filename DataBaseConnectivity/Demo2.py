import cx_Oracle

import os
os.environ['PATH'] = 'C:\\ way of path I dont have Oracle'

# Establish connection to the database

con = cx_Oracle.connect("hr", "hr", "localhost/pdborc1")

cur = con.cursor()

query1 = "insert into student values(102, 'JOHN')"
query2 = "update student set sname = 'XYZ' where sid=102"
query3 = "delete student where sid=102)"


cur.execute(query3)

cur.close()
con.commit()
con.cluse()

print("Completed!!!")

