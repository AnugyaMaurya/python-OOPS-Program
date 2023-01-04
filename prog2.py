'''Write a Python program to demonstrate Polymorphism.
1. Class Vehicle with a parameterized function Fare, that takes input value as fare and
returns it to calling Objects.
2. Create five separate variables Bus, Car, Train, Truck and Ship that call the Fare
function.
3. Use a third variable TotalFare to store the sum of fare for each Vehicle Type.
4. Print the TotalFare.'''

from random import random


class Vehicle:
    def __init__(self):
        self.fare = None

    def Fare(self, fare):
        self.fare = fare


bus, car, train, truck, ship = Vehicle(), Vehicle(), Vehicle(), Vehicle(), Vehicle()
vehicles = [bus, car, train, truck, ship]
for v in vehicles: v.Fare(int(random() * 10))
totalfare = sum([i.fare for i in vehicles])
print(totalfare)