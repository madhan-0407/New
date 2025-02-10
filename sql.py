import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="vglug@123",
    database="Madhan"
)
cursor = conn.cursor()
cursor.execute("""
               CREATE TABLE IF NOT EXISTS employees(
               id INT AUTO_INCREMENT PRIMARY KEY,
               name VARCHAR(30) NOT NULL,
               salary FLOAT,
               created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP )""")

cursor.executemany("INSERT INTO employees (name,salary) VALUES (%s,%s)",("Madhan",30000),("Kumar",20000))
conn.commit()

cursor.execute("SELECT * FROM employees")
rows=cursor.fetchall()
for row in rows:
    print(row)