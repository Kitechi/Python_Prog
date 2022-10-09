import mysql.connector
from datetime import datetime
db = mysql.connector.connect(
    host = "localhost",
    user = "root", 
    passwd = "1234",
    database = "testdatabase")
print ("MySQL Running")

mycursor = db.cursor()

# mycursor.execute("CREATE DATABASE testdatabase")

# mycursor.execute("CREATE TABLE Person(name VARCHAR(50), Age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")

# mycursor.execute("DESCRIBE Person")
# mycursor.execute("INSERT INTO Person(name, age) VALUES ('Salah', 26)")
# mycursor.execute("INSERT INTO Person(name, age) VALUES (%s,%s)", ("Salahuddin", 27))
# db.commit()
# mycursor.execute("SELECT * FROM Person")

# mycursor.execute("CREATE TABLE Test (name varchar(50) NOT NULL, created datetime NOT NULL, gender ENUM ('M', 'F', 'O') NOT NULL, id int PRIMARY KEY NOT NULL AUTO_INCREMENT)")
# mycursor.execute("INSERT INTO Test (name, created, gender) VALUES (%s,%s,%s)", ("Hareera", datetime.now(), "F"))
# db.commit()
# mycursor.execute("SELECT * FROM Test")
# mycursor.execute("SELECT * FROM Test WHERE gender = 'F' ORDER BY id DESC")
mycursor.execute("SELECT id, name FROM Test WHERE gender = 'F' ORDER BY id DESC")
for x in mycursor:
    print(x)