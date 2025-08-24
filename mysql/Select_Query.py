import pymysql as pq

con = pq.connect(host="localhost", user="root", password="", database="echelon")
cursur = con.cursor()
print(
    "{:<20}{:<20}{:<20}{:<20}".format(
        "student_id", "student_name", "student_course", "student_email"
    )
)

try:
    query = "select * from student"
    query1 = "select *from student where st_id=1"
    cursur.execute(query)
    data = cursur.fetchall()
    for i in data:
        print("{:<20}{:<20}{:<20}{:<20}".format(i[0], i[1], i[2], i[3]))
    print()
    cursur.execute(query1)
    data = cursur.fetchall()
    for i in data:
        print("{:<20}{:<20}{:<20}{:<20}".format(i[0], i[1], i[2], i[3]))
except Exception as e:
    print("eror....", e)
