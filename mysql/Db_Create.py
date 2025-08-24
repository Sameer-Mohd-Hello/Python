import pymysql as pq
con = pq.connect(host="localhost", user="root",password="")
cursur = con.cursor()

try:
    db = "create database echelon"
    cursur.execute(db)
    print("database created")
except:
    print("database eror")
