# Defining the base class Vehicle
class Vehicle:
    def move(self):
        pass  

# Defining the Car class that inherits from Vehicle
class Car(Vehicle):
    def move(self):
        print("Driving")

# Defining the Plane class that inherits from Vehicle
class Plane(Vehicle):
    def move(self):
        print("Flying")

# Defining the Bike class that inherits from Vehicle
class Bike(Vehicle):
    def move(self):
        print("Riding")

# Creating instances of each class
car = Car()
plane = Plane()
bike = Bike()

# Using the move() method from each class
car.move()  
plane.move() 
bike.move()  