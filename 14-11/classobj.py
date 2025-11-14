
class Student:
    
    school_name = "MES COLLEGE OF ENGINEERING"

   
    def __init__(self, name, grade):
        self.name = name        
        self.grade = grade      

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Grade: {self.grade}")
        print(f"School: {Student.school_name}")


student1 = Student("Alice", "8th")
student2 = Student("jasir", "3th")


student1.display_details()
student2.display_details()
