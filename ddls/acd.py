import sys
from csv import reader
sys.path.append(r"C:\Users\mohan\Desktop\DataModel-Recent\logg")
sys.path.append(r"C:\Users\mohan\Desktop\DataModel-Recent\connection")
sys.path.append(r"C:\Users\mohan\Desktop\DataModel-Recent\ddls")
import connection
import logfile

class dbconne:
    def __init__(self):
        """Connection with the database is established and the functions for table creation are invoked"""
        try:
            mydb = connection.con()
            mycursor = mydb.cursor()
            print("okay")
            #query = "show tables"
            self.fun_insert(mydb, mycursor)
            #self.select(mydb, mycursor)
            l = logfile.logger()
        except Exception as e:
            l = logfile.logger()
            l.info(e)

    def select(mydb, mycursor):
        try:
            print("okay")
            query = "show tables"
            x = mycursor.execute(query)
            for i in x:
                print(x)
        except Exception as e:
            print(e)
          
            
    def read_txt_file(self, file_path):
        with open (file_path, 'r') as r:
            data = r.readlines()
            return data
    def fun_insert(self, mydb, mycursor):
        try:
           map_dict = {"payment_details": r"C:\Users\mohan\Desktop\DataModel-Recent\prod_data\dimension\payment_dim.csv ",
                    "degree":"C:\\Users\\mohan\\Desktop\\DataModel-Recent\\prod_data\\dimension\\degree_dim.csv",
                     "Exam_details":  r"C:\Users\mohan\Desktop\DataModel-Recent\prod_data\dimension\exams_dim.csv",
                     "Grade_details":  r"C:\Users\mohan\Desktop\DataModel-Recent\prod_data\dimension\grade_dim.csv",
                     "course_details":  r"C:\Users\mohan\Desktop\DataModel-Recent\prod_data\dimension\course_dim.csv",
                     "department_details":  r"C:\Users\mohan\Desktop\DataModel-Recent\prod_data\dimension\department_dim.csv",
                     "staff_details":  r"C:\Users\mohan\Desktop\DataModel-Recent\prod_data\dimension\staff_dim.csv",
                     "placement_details":  r"C:\Users\mohan\Desktop\DataModel-Recent\prod_data\dimension\company_dim.csv",
                     "calendar_details":  r"C:\Users\mohan\Desktop\DataModel-Recent\prod_data\dimension\time_dim.csv"}
            for tbl_nm, file_path in map_dict.items():
                tuple_var = self.read_txt_file(file_path)   
                for row in tuple_var:
                    query = "INSERT INTO " + tbl_nm + " VALUES " + "(" + row + ")"
                    mycursor.execute(query)		
                    mydb.commit()
                    l = logfile.logger()
                    l.info(tbl_nm)
            
        except Exception as error:
            l = logfile.logger()
            l.info(error)
            print(error)
            
        
g = dbconne()	

 