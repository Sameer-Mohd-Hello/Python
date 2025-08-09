import sqlite3
connect = sqlite3.connect("MYDATABASE.db")
connect.execute('''
                Create table Student(
                    st_Id INT AUTO_INCREMENT  KEY,
                    st_Name VARCHAR(50),
                    st_Class VARCHAR(10),
                    st_email VARCHAR(50)
                )
                ''')
connect.close()
