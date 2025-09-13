import pymysql as mq

con = mq.connect(host="localhost", user="root", password="", database="echelon")
cursur = con.cursor()

try:
    print("{:<10}{:<10}".format("count", "fees"))
    que = "select count(*),st_fees from fees group by st_fees"

    cursur.execute(que)
    data = cursur.fetchall()
    for a in data:
        print("{:<10}{:<10}".format(a[0], a[1]))

except Exception as e:
    print("eror", e)
