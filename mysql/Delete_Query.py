import pymysql as pq

con = pq.connect(host="localhost", user="root", password="", database="echelon")
cursur = con.cursor()
id = input("enter st_id to delete ->")
try:
    query = "delete from student where st_id=%s"
    cursur.execute(query, (id))
    con.commit()
    if cursur.rowcount > 0:
        print("student deleted")
    else:
        print("student not present!")
except Exception as e:
    print("eror....", e)
