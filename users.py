class Human:
    def __init__(self,name=None,familyname=None,age=None,gender=None,nationality=None):
        self.list_subject=[]
        self.name=name
        self.familyname=familyname
        self.age=age
        self.gender=gender
        self.nationality=nationality
        
    def set_name(self):
        return self.name
    
    def set_family(self):
        return self.familyname
    
    def set_age(self):
        return self.age
    
    def set_gender(self):
        return self.gender
    
    def set_nationality(self):
        return self.nationality
        
    def get_info(self):
        return {f"{self.name} {self.familyname} is {self.age} years old. Gender is {self.gender}. Nationality is {self.nationality}"}

    
class Student(Human):
    def __init__(self,name=None,familyname=None,age=None,gender=None,nationality=None,school=None,subject=None):
        Human.__init__(self,name=name,familyname=familyname,age=age,gender=gender,nationality=nationality)
        self.school=school
        self.subject=subject
        
    def set_school(self,school=None):
        self.school=school
        return self.school
    
    def add_subject(self,subject=None):
        self.subject=subject
        self.list_subject.append(subject=subject)
            
            
class Teacher(Human):
    def __init__(self,name=None,familyname=None,age=None,gender=None,nationality=None,school=None,subject=None):
        Human.__init__(self,name=name,familyname=familyname,age=age,gender=gender,nationality=nationality)
        self.school=school
        self.subject=subject
        
    def set_subject(self,subject):
        self._subject=subject
        return self.school
    
    def add_subject(self,subject):
        self.list_subject.append(subject=subject)
        
print("Module Users is successfully created")