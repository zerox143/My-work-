#Define students class 
class Student:




#Define students class

 def __init__(self,name,age,grade):
    self._name = name#incapssuation Attricute
    self._age = age#incapssuation Attricute
    self._grade = grade #incapssuation Attricutes
#method to display student information
 def display_info(self):
    print(f"Name:{self._name}, Age:{self._age},Grade:{self._grade}")

#Example usage :


#create a student instance and display information
student1=Student("haseeb",50,"A")
student1.display_info()
