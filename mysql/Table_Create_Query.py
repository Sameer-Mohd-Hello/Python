import pymysql as pq

con = pq.connect(host="localhost", user="root", password="", database="echelon")
cursur = con.cursor()

try:
    db = """create table student(
        st_id INT primary key auto_increment,
        st_name varchar(50),
        st_course varchar(20),
        st_email varchar(50)
        )"""
    cursur.execute(db)
    print("table created")
except:
    print("table eror")
