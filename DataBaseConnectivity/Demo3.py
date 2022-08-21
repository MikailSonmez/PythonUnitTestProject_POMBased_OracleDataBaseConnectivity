import cx_Oracle

import os
os.environ['PATH'] = 'C:\\ way of path I dont have Oracle'

# Establish connection to the database

con = cx_Oracle.connect("hr", "hr", "localhost/pdborc1")

cur = con.cursor()

query = "select * From employees"

cur.execute(query)

for cols in cur:
    print(cols[0], "     ", cols[1], "      ", cols[2])

cur.close()
con.cluse()

print("Completed!!!")
