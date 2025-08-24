import pymysql as pq

con = pq.connect(host="localhost", user="root", password="", database="echelon")
cursur = con.cursor()

try:
    db = "insert into student(st_name,st_course,st_email) values(%s,%s,%s)"
    query = [("jones", "mca", "jones@gmail.com"), ("dery", "mca", "dary@gmail.com")]
    cursur.executemany(db, query)
    con.commit()
    print("values inserted")
except:
    print("table eror")
