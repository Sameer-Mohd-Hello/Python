import pymysql as mq

con = mq.connect(host="localhost", user="root", password="", database="echelon")
cursur = con.cursor()

try:
    que = "select * from student where st_id between 5 and 25"
    cursur.execute(que)
    data = cursur.fetchall()
    for a in data:
        print(a)
except Exception as e:
    print("eror", e)
