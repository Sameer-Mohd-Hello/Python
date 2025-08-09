import sqlite3

connect = sqlite3.connect("MYDATABASE.db")
data = connect.execute("select * from Student where st_Name like '%s%'")
for a in data:
    print(a)
 
