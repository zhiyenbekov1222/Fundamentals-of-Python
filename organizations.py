from education.users import *
import csv
import os.path

class School:
    def __init__(self, name=None, address=None, phone=None, email=None,num_stud=None,num_teachers=None):
        self.name=name
        self.address=address
        self.phone=phone
        self.email=email
        self.num_stud=0
        self.num_teachers=0
        self.list = []
        self.data = []
        self.name_list = []
        self.header = []
        if os.path.exists(f"{name}.csv"):
            with open(f"{name}.csv", "r") as file:
                csv_reader = csv.reader(file)
                for row in csv_reader:
                    if row!=[]:
                        self.data.append(row)
                self.header = self.data[:1]
                self.data = self.data[1:]
                for i in range(len(self.data)):
                    self.name_list.append([self.data[i][0].split()[0], self.data[i][0].split()[1]])
                for elem in self.header:
                    self.name = elem[0].strip()
                    self.address = elem[1].strip() + ", " + elem[2].strip()
                    self.phone = elem[3].strip()
                    self.email=elem[4].strip()
                    self.num_stud=int(elem[5].split()[0])
                    self.num_teachers=int(elem[6].split()[0])
        
    def set_name(self):
        return self.name

    def set_address(self):
        return self.address

    def set_phone(self):
        return self.phone
    
    def set_email(self):
        return self.email
    
    def set_num_stud(self):
        return self.num_stud
    
    def set_num_teachers(self):
        return self.num_teachers 
    
    def add_student(self, name=None, familyname=None, age=None, gender=None, nationality=None):
        for i in range(len(self.name_list)):
            if self.name_list[i][0] == name and self.name_list[i][1] == familyname:
                break
        else:
            self.list.append(Student(name=name, familyname=familyname, age=age, gender=gender, nationality=nationality, school=School.set_name(self)))
            self.num_stud+=1
            
    def add_teacher(self, name=None, familyname=None, age=None, gender=None, nationality=None):
        for i in range(len(self.name_list)):
            if self.name_list[i][0] == name and self.name_list[i][1] == familyname:
                break
        else:
            self.list.append(Teacher(name=name, familyname=familyname, age=age, gender=gender, nationality=nationality, school=School.set_name(self)))
            self.num_teachers+=1
    
    def get_info(self):
        return {f"School name is {self.name}, address is {self.address}, email is {self.email}, phone number is {self.phone}. There are {self.num_stud} students and {self.num_teachers} teachers"}
    
    def get_report(self):
        with open(f"{self.name}.csv", "a", newline="") as file:
            csv_writer=csv.writer(file, delimiter=";")
            if self.header == []:
                csv_writer.writerow(self.get_info())
            for i in self.list:
                csv_writer.writerow(i.get_info())

print("Module with School is imported")