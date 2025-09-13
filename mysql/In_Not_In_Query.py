import pymysql as mq

con = mq.connect(host="localhost", user="root", password="", database="echelon")
cursur = con.cursor()

try:
    print("{:<10}".format("st_name"))
    que = "select st_name from student where st_id in(1,43) "
    queue = "select st_name from student where st_id not in(1,43,44,45) "

    cursur.execute(que)
    data = cursur.fetchall()
    for a in data:
        print("{:<10}".format(a[0]))
       
    print() 
    cursur.execute(queue)
    data = cursur.fetchall()
    for a in data:
        print("{:<10}".format(a[0]))
        
except Exception as e:
    print("eror", e)
