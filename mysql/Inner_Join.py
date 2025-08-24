import pymysql as pq

con = pq.connect(host="localhost", user="root", password="", database="echelon")
cursur = con.cursor()
try:
    print(
        "{:<10}{:<12}{:<15}{:<22}{:<15}".format(
            "st_id", "st_name", "st_course", "st_email", "st_fees"
        )
    )
    query = "select * from student inner join fees on student.st_name=fees.st_name"
    cursur.execute(query)
    data = cursur.fetchall()
    for i in data:
        print("{:<10}{:<12}{:<15}{:<22}{:<15}".format(i[0], i[1], i[2], i[3], i[4]))
except Exception as e:
    print("eror....", e)
