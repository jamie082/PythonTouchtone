import math
import time
# Unit convertions
#variable setting
i = 1
cat = input ("Which category would you like to convert? we support length(l) and Weight(w): ")
unit1 = input ("Which unit would you like to convert from: ")
unit2 = input ("Which unit would you like to convert to: ")

# Calculations

if cat == "l": # Length
    if unit1 == "km" and unit2 == "m":
        km = float(input("Enter the value in km: "))
        m = float(input("Enter the value in m: "))
        m = km * 1000
        print (f"{km} km is equal to {m} m")
    elif unit1 == "m" and unit2 == "km":
        m = float(input("Enter the value in m: "))
        km = float(input("Enter the value in km: "))
        km = m / 1000
        print (f"{m} m is equal to {km} km")

    elif unit1 == "two":
        class myClass:

          def __init__ (self, Model, Description, price):
            self.Model = Model
            self.Description = Description
            self.price = int(price)

          def display_info(self):
              print(f"Name: {self.name}")
              print(f"Age: {self.age}")

              # Accessing attributes and calling methods
              obj.display_info()
              
if cat == "w": # Width
    if unit1 == "kg" and unit2 == "g":
        kg = float(input("Enter the value in kg: "))
        g = float(input("Enter the value in g: "))
        g = kg * 1000
        print (f"{kg} kg is equal to {g} g")
    elif unit1 == "g" and unit2 == "kg":
        g = float(input("Enter the value in g: "))
        kg = g / 1000
        print (f"{g} g is equal to {kg} kg")