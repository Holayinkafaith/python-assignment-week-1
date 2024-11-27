# Defining the Smartphone class
class Smartphone:
    # Constructor to initialize attributes
    def __init__(self, brand, color, model, battery_life):
        self.brand = brand
        self.color = color
        self.model = model
        self.battery_life = battery_life  
    # Method to describe the smartphone
    def describe(self):
        return f"{self.brand} {self.model} in {self.color} with {self.battery_life} hours of battery life."

    # Method to simulate making a call
    def calls(self, contact):
        return f"Calling {contact} from {self.model}..."

# Creating unique objects (instances of the Smartphone class)
phone1 = Smartphone("Apple", "Black", "iPhone 14 Pro", 20)  
phone2 = Smartphone("Samsung", "White", "Galaxy S23 Ultra", 18) 
# Using methods to show details
print(phone1.describe())  
print(phone2.describe())  

# Using the calls method to simulate a call
print(phone1.calls("Olayinka"))
