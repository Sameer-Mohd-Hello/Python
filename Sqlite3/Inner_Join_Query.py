import sqlite3

connect = sqlite3.connect("MYDATABASE.db")
data = connect.execute("select f.st_Name, f.st_Fees from fees as f inner join Student as s on f.st_Id=s.st_Id")

for i in data:
    print(i)
