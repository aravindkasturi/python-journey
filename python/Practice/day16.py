#day16 --> Object Oriented Programming(OOP'S)
"""
OOP (Object-Oriented Programming) is used to organize code so that it is 
easier to write, understand, reuse, and maintain.
"""
#class -blue print off obj
#object - real things that are created from class
#methods -- funtions(study(),drive())
#attributes -- properties(name,age,color)

#constructing objects
#class ---> to be declared in pascal case 
# class CarBlueprint():
# car=CarBlueprint() #object referred to class CarBlueprint

#object attributes
# car.speed 
#object methods
# def move():
#     speed=60
# def stop():
#     speed=0

#python packages
# a package is simply a folder that contains related Python modules (files).
# if a folder contain __init__.py it is a package
from prettytable import PrettyTable  #installed it using pip install prettytable

table = PrettyTable()

table.field_names = ["Name", "Age","IPL Team"]

table.add_row(["Aravind", 23, "RCB"])
table.add_row(["Rahul", 24,"DC"])
table.align='l'  #attribute
print(table)