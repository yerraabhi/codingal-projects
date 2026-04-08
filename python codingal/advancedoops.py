#Create a class with the name Student and perform the following tasks - 1. Declare a variable grade 2. Print a sentence inside the class 3. Create an object of class student and see the output

class Student:
    grade=4
    print("Hello everyone")

ab=Student()
print(ab.grade)

#Create a class Vehicle and perform the following tasks - 1. Create an __init__ method with arguments - max_speed and mileage 2. Create an object of class Vehicle and pass the maximum speed and mileage of the car 3. Print the values of max_speed and mileage by using the object

class Vehicle:
    def __init__(self,maxspeed,mileage):
        self.maxspeed=maxspeed
        self.mileage=mileage
    
modelX=Vehicle(240,18)

print("Model Max Speed:",modelX.maxspeed)
print("Model Mileage:",modelX.mileage)

#Create a class Parrot and perform the following tasks - 1. Create a class variable species 2. Create a __init__ method that has instance variables - name and age 3. Create instances of class Parrot, passing arguments as well 4. Print Class variable by accessing it 5. Print Instance variables as well

class parrot:
    species="bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age

parrot1=parrot("Parro",7)
parrot2=parrot("Parot",5)
print(parrot1.name,"is a",parrot1.species,"and age=",parrot1.age)
print(parrot2.name,"is a",parrot2.species,"and age=",parrot2.age)