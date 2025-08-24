import pymysql as pq

con = pq.connect(host="localhost", user="root", password="", database="echelon")
cursur = con.cursor()
try:
    query = "update student set st_name=%s,st_course=%s,st_email=%s where st_id=24"
    data = ("name", "bca", "name@gmail.com")
    cursur.execute(query, data)
    con.commit()
except Exception as e:
    print("eror....", e)
