import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="vglug@123",
    database="Sample"
)
cursorobject=conn.cursor()

#cursorobject.execute("CREATE DATABASE Sample")
'''
student_record="""CREATE TABLE Student_record(
Rollno INT AUTO_INCREMENT PRIMARY KEY,
Name VARCHAR(30) NOT NULL,
Department VARCHAR(30) NOT NULL,
Age INT)"""


cursorobject.execute("ALTER TABLE Student_record AUTO_INCREMENT=100")
insert="INSERT INTO Student_record ()"

insert="INSERT INTO Student_record (Name,Department,Age) VALUES (%s,%s,%s)"
values=[("Vasanth","CS",21),
        ("Kumar","BCA",21),
        ("Madhu","CyberSecurity",23),
        ("Vasanth","CS",21),
        ("Kumar","BCA",21)]
cursorobject.executemany(insert,values)
conn.commit()
'''
insert="INSERT INTO Student_record (Name,Department,Age) VALUES (%s,%s,%s)"
values=[]
'''
n=int(input("Enter number of data to be insert:"))
if n==1:
        name=input("Enter Name:")
        dept=input("Enter Department:")
        age=int(input("Enter Age:"))
        values.extend([name,dept,age])       
        cursorobject.execute(insert,values)
        conn.commit()
elif n>1:
    #li=[]
    for i in range(n):
        print(f"Enter value for no {i}")
        name=input("Enter Name:")
        dept=input("Enter Department:")
        age=int(input("Enter Age:"))
        #li.extend([name,dept,age])  
        #tup=tuple(li)
        tup=(name,dept,age)
        values.append(tup)

    cursorobject.executemany(insert,values)
    conn.commit()
'''
n=input()
if n==YES or n==Yes or n==yes:
    while True:
        name=input("Enter Name:")
        dept=input("Enter Department:")
        age=int(input("Enter Age:"))
        values.extend([name,dept,age])       
        cursorobject.execute(insert,values)
        conn.commit()
        

#   for i in range(n):tup=tuple(li)
#cursorobject.execute(student_record)
cursorobject.execute("SELECT * FROM Student_record")
rows=cursorobject.fetchall()
for row in rows:
    print(row)