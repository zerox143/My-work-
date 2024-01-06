class student:
    def __init__(self,name,age,roll_number):
        self.name = name #_name is a convertion indication 
        self.age = age
        self.roll_number = roll_number
        #getters
    def get_name(self):
        return self._name
    def get_name (self):
        return self._age
    def get_name (self):
        return self._roll_number
    #setters
    def set_name(self,name):
        self._name = name
    def set_age(self,age):
        self._age = age
    def set_roll_number(self,roll_number):
        student1 =student(name="jhon doe",age=20,roll_number="12345")

        print(f"Name:{student1.get_name ()}")
        print(f"Age:{student1.get_age ()}")
        print(f"Roll number:{student1.get_rollnumber ()}")
       

    