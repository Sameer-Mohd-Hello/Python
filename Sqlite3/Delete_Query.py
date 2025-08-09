import sqlite3

connect = sqlite3.connect("MYDATABASE.db")
st_id = input("enter st_id to delete from database-> ")
connect.execute("delete from Student where st_Id="+st_id)
connect.commit()
connect.close()
