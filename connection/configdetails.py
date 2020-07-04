import configparser

def conpar():
    config = configparser.ConfigParser()
    config.read(r"C:\Users\k.a.ramasubramanian\Desktop\Training\git\DataModel\connection\config.properties")
    host = config.get("dev","host")
    user = config.get("dev", "user")
    password = config.get("dev", "password")
    database = config.get("dev","database")
    print(host, user, password, database)
    return host,user,password,database
#conpar()