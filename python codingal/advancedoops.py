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

#Create a class IOString which consists of a constructor that gives a default value to variable str1. Next up create a method that gets a string as input from the user. Create another method that will print the string in the upper case. Next up create an object and call methods to get everything implemented.

class IOString:
    def __init__(self):
        self.str1=""
    
    def getstring(self):
        self.str1=input("Enter String:")
    
    def printstring(self):
        print("Result is:",self.str1.upper())

str1=IOString()

str1.getstring()
str1.printstring()

#Create a class with the named employee and create a constructor and destructor. Then, write a function to create an object for that class and delete the object. Make sure you call the function to get everything implemented!

class Employee:
    def __init__(self):
        print("Employee created")
    
    def __del__(self):
        print("Destructor called")

def createobj():
    print("Making Object")
    obj=Employee
    print("Function End")
    return obj

print("Calling createobj() function")
obj=createobj()
print("Program End")

#Create a class that will find the numbers in the tuple that add up to a sum and return the position of elements. The value of the sum can be taken as input from the user. Tuple - (10,20,30,40,50,60,70)

class pairelements:
    def twosum(self,nums,target):
        lookup={}

        for i,num in enumerate(nums):
            if target-num in lookup:
                return(lookup[target-num],i)
            lookup[num]==i

value=int(input("Enter sum for which you want to make this search:"))
print("index1=%d, index2=%d" % pairelements().twosum((10,20,30,40,50,60,70),value))