# Define a class named person 
class Person:
    #constructor to initialize the object with name and object 
    def __init__(self, name, age):
        #instance variable to store name and age
        self.name = name
        self.age = age
        #mention to display information about the person 
    def display_info(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        #Define a class name 'student' that in herits from person
class student(Person):
    #constructor to initialize the object with name , age and stucture
    def __init__(self, name, age, student_id):
        #call the constructor of the base class(person) to initialize name ,age 
        super().__init__(name, age)
    #instance variable to store student_id 
        self.student_id = student_id
        #mention to display information about the student
    def display_info(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Student ID: ", self.student_id)
        # call the display info method of base person to print
        super().display_info()
        #print the student 
        print("Student ID: ", {self.student_id})
        #Example usage :
        #create a person object with the name "JOHN DOE" and age 25
        person= Person ("jhon Doe ",25)
        #create a student object with the name "ALICE SMITH" and age 20 and student_id 
        student= student ("<Alice >",20)
        #call the display info method of the person object (Jhon Doe)
        person.display_info()
        #call the display info method of the student object (Alice smith)
        student.display_info()
