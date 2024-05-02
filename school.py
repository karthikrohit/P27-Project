import mysql.connector 


class Connection_db:

    def __init__(self,databse):
        self.db = mysql.connector.connect(
                # host = "127.0.0.1",
                host = "localhost",
                user = "root",
                password = "",
                database = databse
            )
        # self.cursor = self.db.cursor()
        
    def creating_table(self,tableName,tbaleValues):
        try:
            cursor = self.db.cursor()
            query = f"create table {tableName} {tbaleValues}"
            print(query)
            cursor.execute(query)
            print('Success Table Created')
            print(100*'-')
        except Exception as e:
            print('Error')
            print(e)

    def addDataToTable(self,tableName,fieldstoadd,values):
        try:
            cursor = self.db.cursor()
            query = f"insert into {tableName} {fieldstoadd} values {values}"
            cursor.execute(query)
            self.db.commit()
            print('Data successfully added to the table')
        except Exception as e:
            print(e)
            print('Error')

    def toreadData(self,tableName):
        try:
            cursor = self.db.cursor()
            query = f"select * from {tableName}"
            cursor.execute(query)
            value = cursor.fetchall()
            return value
        except:
            print('Error')

    def question_method(self):
        try:
            quesion = input('1 for read the data\n2 for Insert a new data\n3 for Update a new data\n4 for delete a data:\n')
            return quesion
        except:
            print('Error')
    
    def get_values(self,column_to_be_added):
        datas = tuple([i for i in re.split('[(,)]',column_to_be_added) if i])
        out_data = tuple([input(f'{i}: ') for i in datas])
        # print(out_data)
        return out_data
    
    def get_update_value(self,tableName,idName,id,fieldtoUpdate,newvalue):
        try:
            cursor = self.db.cursor()
            query = f"update {tableName} set {fieldtoUpdate}={newvalue} where {idName} = {id}"
            cursor.execute(query)
            self.db.commit()
            print('The data got Updated')
        except:
            print('Error in update')

    def delete_data_from_table(self,tableName,idName,id):
        try:
            cursor = self.db.cursor()
            query = f"delete from {tableName} where {idName}='{id}'"
            cursor.execute(query)
            print('It is Successfullly deleted')
            self.db.commit()
        except:
            print('It is Failed to be deleted')




conn_new = Connection_db("school")

# step1:
#conn_new.creating_table('Student','(studentId int auto_increment primary key , studentName varchar(255), PythonMark int, MathMark int, PhysicsMark int)')

#conn_new.creating_table('Teacher','(TeacherId int auto_increment primary key, TeacherName varchar(255), Teachersalary int, Teacherjoiningdate datetime)')


#conn_new.creating_table('Principal','(TeacherId int, TeacherName varchar(255), Teachersalary int, Teacherjoiningdate datetime)')

#conn_new.creating_table('Admin','(adminId int auto_increment primary key, adminName varchar(255), password varchar(255))')

# step2:
#conn_new.addDataToTable('admin','(adminName,password)',("anu",'1234'))
#conn_new.addDataToTable('admin','(adminName,password)',("iniya",'9876'))

#conn_new.addDataToTable('Student','(studentName,PythonMark,MathMark,PhysicsMark)',('akila',  '10', '71', '21'))
#conn_new.addDataToTable('Student','(studentName,PythonMark,MathMark,PhysicsMark)',('mano',  '81', '12', '31'))
#conn_new.addDataToTable('Student','(studentName,PythonMark,MathMark,PhysicsMark)',('raju',  '41', '12', '41'))
#conn_new.addDataToTable('Student','(studentName,PythonMark,MathMark,PhysicsMark)',('aakash',  '61', '19', '71'))

#conn_new.addDataToTable('Teacher','(TeacherName,Teachersalary,Teacherjoiningdate)',('prakash',5000,'2024-01-27'))
#conn_new.addDataToTable('Teacher','(TeacherName,Teachersalary,Teacherjoiningdate)',('vino',8000,'2024-01-27'))
#conn_new.addDataToTable('Teacher','(TeacherName,Teachersalary,Teacherjoiningdate)',('dinesh',10000,'2024-01-27' ))
#conn_new.addDataToTable('Teacher','(TeacherName,Teachersalary,Teacherjoiningdate)',('meenachi',40000,'2024-01-27'))
#conn_new.addDataToTable('Teacher','(TeacherName,Teachersalary,Teacherjoiningdate)',('Harish',20000,'2024-01-27'))
#conn_new.addDataToTable('Teacher','(TeacherName,Teachersalary,Teacherjoiningdate)',('Praganesh',15000,'2024-01-27'))

#conn_new.addDataToTable('Principal','(TeacherId,TeacherName,Teachersalary,Teacherjoiningdate)',(4,'meenachi',40000,'2024-01-27'))





import re

# step3:
admin_check = False
while not admin_check:
    adminId = input('Enter Your AdminId: ')
    adminPasswd = input('Enter Your adminPasswd: ')
    data_admin = conn_new.toreadData('Admin')
    # for i in data_admin:
    #     print(i)
    for i in data_admin:
        if int(adminId) == i[0] and adminPasswd == i[-1]:
            admin_check  = True
    if admin_check:
        print('You are a valid Admin')
        selection_admin = input('What you wanted to see\n1 for Students\n2 for Teacher\n3 for Principal:\n')

        if selection_admin == '1': # student
            tableName = 'Student'
            column_to_be_added = '(studentName,PythonMark,MathMark,PhysicsMark)'
            # values = conn_new.question_method()
            print()
            print('You have Entered into Student Section')
            print()
            select_output = conn_new.question_method()
            if select_output == '1': # read
                print('Inside reading data')
                select_output = conn_new.toreadData(tableName)
                print("The Student Details")
                print(select_output)
            elif select_output == '2': # Insert
                select_output = conn_new.get_values(column_to_be_added)
                print(select_output)
                conn_new.addDataToTable('Student',column_to_be_added,select_output)
            elif select_output == '3': # Update
                tableName = 'Student'
                id = int(input('Enter the StudentId for which you want to update'))
                fieldtoUpdate = input('Enter the columnName for which you want to update')
                newvalue = input('Enter the NewData for which you want to update')
                idName = 'studentId'
                conn_new.get_update_value(tableName,idName,id,fieldtoUpdate,newvalue)
            elif select_output == '4':
                tableName = 'Student'
                id = int(input('Enter the StudentId for which you want to delete'))
                idName = 'studentId'
                conn_new.delete_data_from_table(tableName,idName,id)

        elif selection_admin == '2': # teacher
            tableName = 'Teacher'
            column_to_be_added = '(TeacherName,Teachersalary,Teacherjoiningdate)'
            # values = conn_new.question_method()
            print()
            print('You have Entered into Teacher Section')
            print()
            select_output = conn_new.question_method()
            if select_output == '1': # read
                print('Inside reading data')
                select_output = conn_new.toreadData(tableName)
                print("The Student Details")
                print(select_output)
            elif select_output == '2': # Insert
                select_output = conn_new.get_values(column_to_be_added)
                print(select_output)
                conn_new.addDataToTable('Teacher',column_to_be_added,select_output)

        elif selection_admin == '3': # principal
            print('You have Entered into Principal Section')
            print()
            conn_new.question_method()

    else:
        print('You are not a valid Admin enter proper Credentials')

        

