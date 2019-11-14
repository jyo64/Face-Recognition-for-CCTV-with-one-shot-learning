import os
import sys
import time
import mysql.connector

def dbupdate():
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="root",database="facedb")
    mycursor = mydb.cursor()
    dir = os.path.join(os.getcwd(),'detected')
    #print(dir)
    list1 = os.listdir(dir)

    #print(list1)
    for x in list1 :        
        #print(x," Detected!!")
        sql ="UPDATE userdata SET found = 1 WHERE name =%s " 
        val = (x,)       
        mycursor.execute(sql,val)
        mydb.commit()
    
while True :
    dbupdate()
    dir = os.path.join(os.getcwd(),'detected')
    list = os.listdir(dir)
    prevlen = len(list)



    time.sleep(5)

    dir = os.path.join(os.getcwd(),'detected')
    list = os.listdir(dir)
    curlen = len(list)

    if curlen != prevlen :
        print("Entry Add or Delete Detected")
        dbupdate()