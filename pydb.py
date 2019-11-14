import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="facedb"
)

print(mydb) 

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM userdata")

myresult = mycursor.fetchall()
print(myresult)
for x in myresult:
  print(x)