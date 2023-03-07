'''Program name : Vehicle.py
 Author : EMMANUEL ADEBANJO
 Date last updated : 03 / 05 / 2023
 Purpose : an app that will accept user input for a car.The app will then ask the user for the year, make, model, doors, and type of roof and store the data. The app will then output the data collected.
 '''

 # super class with custrutor
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

# child class
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        # invoking vehicle class constructor
        Vehicle.__init__(self, vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

#accepting user input        
type_i=input("Enter Vehicle type (car, truck, plane, boat) : ")
year_i=input("Enter the year : ")
make_i=input("Enter the make : ")
model_i=input("Enter the model : ")
doors_i=input("Enter the number of doors(2 or 4) : ")
roof_i=input("Type of roof (solid or sun roof) : ")
#calling the constructor
A=Automobile(type_i,year_i,make_i,model_i,doors_i,roof_i) 

#print deatils
print("\nVehicle type : "+A.vehicle_type)
print("\nYear : "+A.year)
print("\nMake : "+A.make)
print("\nModel : "+A.model)
print("\nNumber of doors : "+A.doors)
print("\nType of roof : "+A.roof)
