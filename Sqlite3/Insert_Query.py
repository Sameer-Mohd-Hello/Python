import sqlite3
connect = sqlite3.connect("MYDATABASE.db")
val = '''insert into Student(st_Name, st_Class, st_email) 
values("aakash", "MCA", "aakash02032005@gmail.com"),
("shivam", "MCA", "shivam02032005@gmail.com")'''
connect.execute(val)
connect.commit()
connect.close()
