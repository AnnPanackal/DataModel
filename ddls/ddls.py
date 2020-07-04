from connection import connection
from logg import logfile
from csv import reader
from datetime import datetime


class dbconn:
    def __init__(self):
        """Connection with the database is established and the functions for table creation are invoked"""
        try:
            mydb = connection.con()
            mycursor = mydb.cursor()
            self.createSTUDENT_REFERENCE(mydb, mycursor)
            self.createFpayment(mydb, mycursor)
            self.createFacademics(mydb, mycursor)
            self.createFstudent(mydb, mycursor)
            self.createFattendence(mydb, mycursor)
            self.createFplacement(mydb, mycursor)

            self.PaymentDetails(mydb, mycursor)
            self.Degree(mydb, mycursor)
            self.ExamDetails(mydb, mycursor)
            self.GradeDetails(mydb, mycursor)
            self.CourseDetails(mydb, mycursor)
            self.DepartmentDetails(mydb, mycursor)
            self.StaffDetails(mydb, mycursor)
            self.CalenderDetails(mydb, mycursor)
            self.PlacementDetails(mydb, mycursor)

            '''self.insertSTUDENT_REFERENCE(mydb, mycursor)
            self.insertFpayment(mydb,mycursor)
            self.insertFacademics(mydb,mycursor)
            self.insertFplacement(mydb,mycursor)
            self.insertFstudent(mydb,mycursor)'''
            self.insertFattendence(mydb,mycursor)
        except Exception as e:
            print("Error:",e)

    def createSTUDENT_REFERENCE(self, mydb, mycursor):
        """Creation of student reference table which contains details of the student."""
        try:
            sql='''create table if not exists STUDENT_REFERENCE(STUDENT_ID BIGINT PRIMARY KEY NOT NULL,
                     NAME     VARCHAR(45)   NOT NULL,
                     DOB       DATE       NOT NULL,
                     GENDER    VARCHAR(10),
                     GUARDIAN_NAME  VARCHAR(45),
                     ADDRESS    VARCHAR(50),
                     PHONE_NO   BIGINT,
                     DOJ    DATE,
                     STUDENT_START_DATE DATETIME,
                     STUDENT_END_DATE   DATETIME)'''
            #mycursor.execute("drop table student_reference")
            mycursor.execute(sql)
            mydb.commit()
            l = logfile.logger()
            l.info("STUDENT_REFERENCE created!")
        except Exception as e:
            print("Error:", e)

    def createFpayment(self, mydb, mycursor):
        """Creation of fact table for payment."""
        try:
            sql='''create table if not exists FactPayment(STUDENT_ID BIGINT NOT NULL,
                     FEE_ID    VARCHAR(10)   NOT NULL,
                     PAYMENT_ID VARCHAR(9),
                     PAYMENT_FACT_START_DATE DATETIME,
                     PAYMENT_FACT_END_DATE   DATETIME)'''
            #mycursor.execute("drop table FactPayment")
            mycursor.execute(sql)
            mydb.commit()
            l = logfile.logger()
            l.info("Fact : Payment created!")
        except Exception as e:
            print("Error:", e)

    def createFacademics(self, mydb, mycursor):
        """Creation of fact table for academics."""
        try:
            sql='''create table if not exists FactAcademics(STUDENT_ID BIGINT NOT NULL,
                     DEGREE_ID  BIGINT,
                     EXAM_ID    INT,
                     MARKS  INT,
                     COURSE_ID  VARCHAR(9),
                     GRADE_ID   CHAR(2),
                     ACADEMICS_START_DATE DATETIME,
                     ACADEMICS_END_DATE   DATETIME)'''
            #mycursor.execute("drop table FactAcademics")
            mycursor.execute(sql)
            mydb.commit()
            l = logfile.logger()
            l.info("Fact : Academics created!")
        except Exception as e:
            print("Error:", e)

    def createFstudent(self, mydb, mycursor):
        """Creation of fact table for student."""
        try:
            sql='''create table if not exists FactStudent(STUDENT_ID BIGINT NOT NULL,
                     DEP_ID    VARCHAR(9)   NOT NULL,
                     COURSE_ID VARCHAR(9),
                     STAFF_ID   VARCHAR(9),
                     STUDENT_FACT_START_DATE DATETIME,
                     STUDENT_FACT_END_DATE   DATETIME)'''
            #mycursor.execute("drop table FactStudent")
            mycursor.execute(sql)
            mydb.commit()
            l = logfile.logger()
            l.info("Fact : Student created!")
        except Exception as e:
            print("Error:", e)

    def createFattendence(self, mydb, mycursor):
        """Creation of fact table for attendance."""
        try:
            sql='''create table if not exists FactAttendence(STUDENT_ID BIGINT NOT NULL,
                     TIME_ID    VARCHAR(5),
                     CURDATE    DATE,
                     COURSE_ID  VARCHAR(9),
                     STAFF_ID   VARCHAR(9),
                     ATTENDENCE VARCHAR(5),
                     ATTENDENCE_START_DATE DATETIME,
                     ATTENDENCE_END_DATE   DATETIME)'''
            #mycursor.execute("drop table FactAttendence")
            mycursor.execute(sql)
            mydb.commit()
            l = logfile.logger()
            l.info("FACT : Attendence created!")
        except Exception as e:
            print("Error:", e)

    def createFplacement(self, mydb, mycursor):
        """Creation of fact table for placement."""
        try:
            sql='''create table if not exists FactPlacement(STUDENT_ID BIGINT NOT NULL,
                     DEP_ID    VARCHAR(9),
                     COMPANY_ID VARCHAR(9),
                     HIRED  VARCHAR(5),
                     PLACEMENT_FACT_START_DATE DATETIME,
                     PLACEMENT_FACT_END_DATE   DATETIME)'''
            #mycursor.execute("drop table FactPlacement")
            mycursor.execute(sql)
            mydb.commit()
            l = logfile.logger()
            l.info("Fact : Placement created!")
        except Exception as e:
            print("Error:", e)

    def PaymentDetails(self, mydb, mycursor):
        """Creation of dimension table for payment details."""
        try:
            sql = '''create table if not exists payment_details(FEE_ID VARCHAR(10) NOT NULL PRIMARY KEY,
                        FEES   BIGINT,
                        FEES_TYPE  VARCHAR(15),
                        PAYMENT_START_DATE DATETIME,
                        PAYMENT_END_DATE   DATETIME)'''
            #mycursor.execute("drop table payment_details")
            mycursor.execute(sql)
            mydb.commit()
            l = logfile.logger()
            l.info("DIMENSION : Payment_Details created!")
        except Exception as e:
            print("Error:", e)

    def Degree(self, mydb, mycursor):
        """Creation of dimension table for degree."""
        try:
            sql = '''create table if not exists degree(DEGREE_ID BIGINT NOT NULL PRIMARY KEY,
                        DEGREE_TYPE   VARCHAR(5),
                        DURATION   INT,
                        DEGREE_START_DATE DATETIME,
                        DEGREE_END_DATE   DATETIME)'''
            #mycursor.execute("drop table degree")
            mycursor.execute(sql)
            mydb.commit()
            l = logfile.logger()
            l.info("DIMENSION : Details created!")
        except Exception as e:
            print("Error:", e)

    def ExamDetails(self, mydb, mycursor):
        """Creation of dimension table for exam details."""
        try:
            sql = '''create table if not exists exam_details(EXAM_ID INT NOT NULL PRIMARY KEY,
                        EXAM_TYPE   VARCHAR(3),
                        EXAM_DESCRIPTION    VARCHAR(15),
                        EXAM_START_DATE DATETIME,
                        EXAM_END_DATE   DATETIME)'''
            #mycursor.execute("drop table exam_details")
            mycursor.execute(sql)
            mydb.commit()
            l = logfile.logger()
            l.info("DIMENSION : Exam_Details created!")
        except Exception as e:
            print("Error:", e)

    def GradeDetails(self, mydb, mycursor):
        """Creation of dimension table for grade details."""
        try:
            sql = '''create table if not exists grade_details(GRADE_ID CHAR(2) NOT NULL PRIMARY KEY,
                        GRADE_DESCRIPTION    CHAR(20),
                        GRADE_START_DATE DATETIME,
                        GRADE_END_DATE   DATETIME)'''
            #mycursor.execute("drop table grade_details")
            mycursor.execute(sql)
            mydb.commit()
            l = logfile.logger()
            l.info("DIMENSION : Grade_Details created!")
        except Exception as e:
            print("Error:", e)

    def CourseDetails(self, mydb, mycursor):
        """Creation of dimension table for course details."""
        try:
            sql = '''create table if not exists course_details(COURSE_ID VARCHAR(9) NOT NULL PRIMARY KEY,
                        COURSE_NAME VARCHAR(20),
                        COURSE_START_DATE DATETIME,
                        COURSE_END_DATE   DATETIME)'''
            #mycursor.execute("drop table course_details")
            mycursor.execute(sql)
            mydb.commit()
            l = logfile.logger()
            l.info("DIMENSION : Course_Details created!")
        except Exception as e:
            print("Error:", e)

    def DepartmentDetails(self, mydb, mycursor):
        """Creation of dimension table for  department details."""
        try:
            sql = '''create table if not exists department_details(DEP_ID VARCHAR(9) NOT NULL PRIMARY KEY,
                        DEP_NAME VARCHAR(20),
                        DEP_START_DATE DATETIME,
                        DEP_END_DATE   DATETIME)'''
            #mycursor.execute("drop table department_details")
            mycursor.execute(sql)
            mydb.commit()
            l = logfile.logger()
            l.info("DIMENSION : Dep_Details created!")
        except Exception as e:
            print("Error:", e)

    def StaffDetails(self, mydb, mycursor):
        """Creation of dimension table for  staff details."""
        try:
            sql = '''create table if not exists staff_details(STAFF_ID VARCHAR(9) NOT NULL PRIMARY KEY,
                        STAFF_NAME VARCHAR(25),
                        STAFF_DOJ   DATE,
                        STAFF_START_DATE DATETIME,
                        STAFF_END_DATE   DATETIME)'''
            #mycursor.execute("drop table staff_details")
            mycursor.execute(sql)
            mydb.commit()
            l = logfile.logger()
            l.info("DIMENSION : Staff_Details created!")
        except Exception as e:
            print("Error:", e)

    def CalenderDetails(self, mydb, mycursor):
        """Creation of dimension table for  calender details."""
        try:
            sql = '''create table if not exists calender_details(TIME_ID VARCHAR(5) NOT NULL PRIMARY KEY,
                        HOLIDAY DATE,
                        HOLIDAY_START_DATE DATETIME,
                        HOLIDAY_END_DATE   DATETIME)'''
            #mycursor.execute("drop table calender_details")
            mycursor.execute(sql)
            mydb.commit()
            l = logfile.logger()
            l.info("DIMENSION : Calender_Details created!")
        except Exception as e:
            print("Error:", e)

    def PlacementDetails(self, mydb, mycursor):
        """Creation of dimension table for  placement details."""
        try:
            sql = '''create table if not exists placement_details(COMPANY_ID VARCHAR(9) NOT NULL PRIMARY KEY,
                        COMPANY_NAME    VARCHAR(15),
                        PLACEMENT_VENUE VARCHAR(50),
                        PLACEMENT_DATE  DATE,
                        PLACEMENT_START_DATE DATETIME,
                        PLACEMENT_END_DATE   DATETIME)'''
            #mycursor.execute("drop table placement_details")
            mycursor.execute(sql)
            mydb.commit()
            l = logfile.logger()
            l.info("DIMENSION : Placement_Details created!")
        except Exception as e:
            print("Error:", e)

    def insertSTUDENT_REFERENCE(self, mydb, mycursor):
        """insertion of student reference table which contains details of the student."""
        try:
            with open(r"C:\Users\k.a.ramasubramanian\Desktop\Training\git\DataModel\prod_data\reference\student_reference.csv") as data:
                for i in reader(data):
                    sql = "INSERT INTO STUDENT_REFERENCE VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    val = (i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],datetime.now(),i[9])
                    mycursor.execute(sql, val)
                    mydb.commit()
            print("No. of rows inserted:", mycursor.rowcount)
            l = logfile.logger()
            l.info("STUDENT_REFERENCE-RECORDS inserted")
            print("Rows Inserted")
        except Exception as e:
            print("Error:", e)
    def insertFpayment(self,mydb, mycursor):
        """insertion of payment fact table which contains details of the student."""
        try:
            with open(r"C:\Users\k.a.ramasubramanian\Desktop\Training\git\DataModel\prod_data\fact\payment_fact.csv") as data:
                #s = csv.reader(data)
                for i in reader(data):
                    sql = "INSERT INTO factpayment VALUES(%s,%s,%s,%s,%s)"
                    val = (i[0],i[1],i[2],datetime.now(),i[4])
                    mycursor.execute(sql, val)
                    mydb.commit()
            print("No. of rows inserted:", mycursor.rowcount)
            l = logfile.logger()
            l.info("FACT_PAYMENT-RECORDS inserted")
            print("Rows Inserted")
        except Exception as e:
            print("Error:", e)
    def insertFpayment(self,mydb, mycursor):
        """insertion of payment fact table which contains details of the student."""
        try:
            with open(r"C:\Users\k.a.ramasubramanian\Desktop\Training\git\DataModel\prod_data\fact\payment_fact.csv") as data:
                for i in reader(data):
                    sql = "INSERT INTO factpayment VALUES(%s,%s,%s,%s,%s)"
                    val = (i[0],i[1],i[2],datetime.now(),i[4])
                    mycursor.execute(sql, val)
                    mydb.commit()
            print("No. of rows inserted:", mycursor.rowcount)
            l = logfile.logger()
            l.info("FACT_PAYMENT-RECORDS inserted")
            print("Rows Inserted")
        except Exception as e:
            print("Error:", e)
    def insertFacademics(self,mydb,mycursor):
        """insertion of academics fact table which contains details of the student."""
        try:
            with open(r"C:\Users\k.a.ramasubramanian\Desktop\Training\git\DataModel\prod_data\fact\academics_fact.csv") as data:
                for i in reader(data):
                    sql = "INSERT INTO factacademics VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
                    val = (i[0], i[1], i[2], i[3],i[4],i[5],datetime.now(), i[7])
                    mycursor.execute(sql, val)
                    mydb.commit()
            print("No. of rows inserted:", mycursor.rowcount)
            l = logfile.logger()
            l.info("FACT_ACADEMICS-RECORDS inserted")
            print("Rows Inserted")
        except Exception as e:
            print("Error:", e)
    def insertFplacement(self,mydb, mycursor):
        """insertion of placement fact table which contains details of the student."""
        try:
            with open(r"C:\Users\k.a.ramasubramanian\Desktop\Training\git\DataModel\prod_data\fact\placement_fact.csv") as data:
                for i in reader(data):
                    sql = "INSERT INTO factplacement VALUES(%s,%s,%s,%s,%s,%s)"
                    val = (i[0], i[1], i[2], i[3],datetime.now(), i[5])
                    mycursor.execute(sql, val)
                    mydb.commit()
            print("No. of rows inserted:", mycursor.rowcount)
            l = logfile.logger()
            l.info("FACT_PLACEMENT-RECORDS inserted")
            print("Rows Inserted")
        except Exception as e:
            print("Error:", e)
    def insertFstudent(self,mydb, mycursor):
        """insertion of placement fact table which contains details of the student."""
        try:
            with open(r"C:\Users\k.a.ramasubramanian\Desktop\Training\git\DataModel\prod_data\fact\student_fact.csv") as data:
                for i in reader(data):
                    sql = "INSERT INTO factstudent VALUES(%s,%s,%s,%s,%s,%s)"
                    val = (i[0], i[1], i[2], i[3],datetime.now(), i[5])
                    mycursor.execute(sql,val)
                    mydb.commit()
            print("No. of rows inserted:", mycursor.rowcount)
            l = logfile.logger()
            l.info("FACT_STUDENT-RECORDS inserted")
            print("Rows Inserted")
        except Exception as e:
            print("Error:", e)
    def insertFattendence(self,mydb, mycursor):
        """insertion of placement fact table which contains details of the student."""
        try:
            with open(r"C:\Users\k.a.ramasubramanian\Desktop\Training\git\DataModel\prod_data\fact\attendance_fact.csv") as data:
                for i in reader(data):
                    sql = "INSERT INTO factattendence VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
                    val = (i[0], i[1], i[2], i[3],i[4],i[5],datetime.now(), i[7])
                    mycursor.execute(sql,val)
                    mydb.commit()
            print("No. of rows inserted:", mycursor.rowcount)
            l = logfile.logger()
            l.info("FACT_STUDENT-RECORDS inserted")
            print("Rows Inserted")
        except Exception as e:
            print("Error:", e)

obj=dbconn()



