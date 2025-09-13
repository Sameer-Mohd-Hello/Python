import pymysql as mq

con = mq.connect(host="localhost", user="root", password="", database="echelon")
cursur = con.cursor()

try:
    print("{:<10}".format("fees"))
    que = "select sum(st_fees) from fees "

    cursur.execute(que)
    data = cursur.fetchall()
    for a in data:
        print("{:<10}".format(a[0]))

except Exception as e:
    print("eror", e)
