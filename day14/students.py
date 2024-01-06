#Define students class 
class Student:




#Define students class

 def __init__(self,name,age,grade):
    self.name = name
    self.age = age
    self.grade = grade 
#method to display student information
 def display_info(self):
    print(f"Name:{self.name}, Age:{self.age},Grade:{self.grade}")

#Example usage :


#create a student instance and display information
student1=Student("haseeb",50,"A")
student1.display_info()
