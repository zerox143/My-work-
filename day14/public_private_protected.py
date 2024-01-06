#Define class name car
class Car:
   #construtor mrthod to intialize objec attributes
    def __init__(self,make,model,year):
     #private attributes pre fixed with double under score
     self.__make = make
     #producted attributes prefixed with a signle under score 
     self.__model = model
    #Public attributes 
     self.__year = year
   #public method to display information about car
   
    def display_info(self):
       print(f"Make:{self.__make}, Model:{self.__model}, Year:{self.__year}")
   #public method to start the car
    def start_car(self):
       #invoking a private method with in the class
       self.__display_info()
       print("Engine started")
   # creating an instance of the car 
my_car = Car("Ford","Mustang",2020)
    #Acessing public attribute directly
print(f"car year:{my_car.year}")
print(f"car modle:{my_car.__model}")
     