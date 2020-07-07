import pytest
import sys
sys.path.append(r'C:\Users\mohan\Desktop\DataModel-Recent\connection')
import connection

class Testinsertion():
    def test_fact_academics(self):
        mydb = connection.con()
        mycursor = mydb.cursor()
        sql = '''select * from factacademics where not exists(select * from test_factacademics)'''
        res = mycursor.execute(sql)
        assert res == None

    def test_fact_attendence(self):
        mydb = connection.con()
        mycursor = mydb.cursor()
        sql = '''select * from factattendence where not exists(select * from test_factattendence)'''
        res = mycursor.execute(sql)
        assert res == None

    def test_fact_payment(self):
        mydb = connection.con()
        mycursor = mydb.cursor()
        sql = '''select * from factpayment where not exists(select * from test_factpayment)'''
        res = mycursor.execute(sql)
        assert res == None

    def test_fact_placement(self):
        mydb = connection.con()
        mycursor = mydb.cursor()
        sql = '''select * from factplacement where not exists(select * from test_factplacement)'''
        res = mycursor.execute(sql)
        assert res == None

    def test_fact_student(self):
        mydb = connection.con()
        mycursor = mydb.cursor()
        sql = '''select * from factstudent where not exists(select * from test_factstudent)'''
        res = mycursor.execute(sql)
        assert res == None

    def test_dim_calender(self):
        mydb = connection.con()
        mycursor = mydb.cursor()
        sql = '''select * from calender_details where not exists(select * from test_calender_details)'''
        res = mycursor.execute(sql)
        assert res == None

    def test_dim_course(self):
        mydb = connection.con()
        mycursor = mydb.cursor()
        
        sql = '''select * from course_details where not exists(select * from test_course_details)'''
        res = mycursor.execute(sql)
        assert res == None

    def test_dim_degree(self):
        mydb = connection.con()
        mycursor = mydb.cursor()
        sql = '''select * from degree where not exists(select * from test_degree)'''
        res = mycursor.execute(sql)
        assert res == None

    def test_dim_department(self):
        mydb = connection.con()
        mycursor = mydb.cursor()
        sql = '''select * from department_details where not exists(select * from test_department_details)'''
        res = mycursor.execute(sql)
        assert res == None

    def test_dim_exam(self):
        mydb = connection.con()
        mycursor = mydb.cursor()
        sql = '''select * from exam_details where not exists(select * from test_exam_details)'''
        res = mycursor.execute(sql)
        assert res == None

    def test_dim_grade(self):
        mydb = connection.con()
        mycursor = mydb.cursor()
        sql = '''select * from grade_details where not exists(select * from test_grade_details)'''
        res = mycursor.execute(sql)
        assert res == None

    def test_dim_payment(self):
        mydb = connection.con()
        mycursor = mydb.cursor()
        sql = '''select * from payment_details where not exists(select * from test_payment_details)'''
        res = mycursor.execute(sql)
        assert res == None

    def test_dim_placement(self):
        mydb = connection.con()
        mycursor = mydb.cursor()
        sql = '''select * from placement_details where not exists(select * from test_placement_details)'''
        res = mycursor.execute(sql)
        assert res == None

    def test_dim_staff(self):
        mydb = connection.con()
        mycursor = mydb.cursor()
        sql = '''select * from staff_details where not exists(select * from test_staff_details)'''
        res = mycursor.execute(sql)
        assert res == None

    def test_ref_student(self):
        mydb = connection.con()
        mycursor = mydb.cursor()
        sql = '''select * from student_reference where not exists(select * from test_student_reference)'''
        res = mycursor.execute(sql)
        assert res == None


obj=Testinsertion()
obj.test_fact_academics()