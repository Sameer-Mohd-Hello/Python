import pymysql as mq

con = mq.connect(host="localhost", user="root", password="", database="echelon")
cursur = con.cursor()

try:
    que = "select * from fees where st_fees=(select min(st_fees) from fees)"
    queue = "select * from fees where st_fees=(select max(st_fees) from fees)"

    cursur.execute(que)
    data = cursur.fetchall()
    for a in data:
        print(a)
    print()
    cursur.execute(queue)
    data = cursur.fetchall()
    for a in data:
        print(a)

except Exception as e:
    print("eror", e)
