import cx_Oracle

import os
os.environ['PATH'] = 'C:\\ way of path I dont have Oracle'

# Establish connection to the database

con = cx_Oracle.connect("hr", "hr", "localhost/pdborcl")

print("Connected!!!")

con.close()

