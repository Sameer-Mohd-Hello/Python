import pymysql as pq

con = pq.connect(host="localhost", user="root", password="", database="echelon")
cursur = con.cursor()
try:
    print("{:<10}{:<12}{:<22}{:<22}".format("st_id", "st_name", "st_email", "st_fees"))
    query = "select student.st_id, student.st_name, student.st_email, fees.st_fees from student right join fees on student.st_name=fees.st_name"
    cursur.execute(query)
    data = cursur.fetchall()
    for i in data:
        st_fees = i[3] if i[3] is not None else "N/A"
        print("{:<10}{:<12}{:<22}{:<22}".format(i[0], i[1], i[2], st_fees))
except Exception as e:
    print("eror....", e)
