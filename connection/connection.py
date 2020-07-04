import mysql.connector
from connection import configdetails

def con():
    host, user, pwd, db = configdetails.conpar()
    mydb = mysql.connector.connect(host=host, user=user, password=pwd, database=db)
    #print(mydb.is_connected())
    return mydb
#scon()