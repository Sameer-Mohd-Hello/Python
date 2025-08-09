import sqlite3

connect = sqlite3.connect("MYDATABASE.db")
data = connect.execute("select * from student limit 0,2")
print("s_id", "", "s_name", "   ", "s_class", "  ", "s_email")
for a in data:
    print(a[0], "   ", a[1], "   ", a[2], "   ", a[3])
