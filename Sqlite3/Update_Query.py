import sqlite3

connect = sqlite3.connect("MYDATABASE.db")
connect.execute("update Student set st_Name='sameer ali' where st_Id=1")
connect.commit()
connect.close()
