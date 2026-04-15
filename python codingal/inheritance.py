#Implement Inheritance by creating a Parent Class Vehicle with a constructor that has details like name, maximum speed, and mileage. Then, create a Child Class Bus that inherits Class Vehicle. Finally, showcase Inheritance to display the details of the Vehicle Bus named - School Volvo.

class Vehicle:
    def __init__(self,name,maxspeed,mileage):
        self.name=name
        self.maxspeed=maxspeed
        self.mileage=mileage

class Bus(Vehicle):
    pass

Schoolbus=Bus("School Volvo",180,12)

print("School Bus Name:",Schoolbus.name,"Speed:",Schoolbus.maxspeed,"Mileage:",Schoolbus.mileage)

#Create a parent class Person (attributes - name, id number) with a method display to display the attributes. Next, create a child class Employee (attributes - name, id number, salary, post). Access the attributes of parent class in child class. Then, create an object for child class and call the display method to display the name and id number.

class Person:
    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber
    
    def display(self):
        print("Name=",self.name)
        print("idnumber=",self.idnumber)

class Employee(Person):
    def __init__(self,name,idnumber,salary,post):
        self.salary=salary
        self.post=post
        Person.__init__(self,name,idnumber)

a=Employee("Rahul",886012,200000,"Intern")

a.display()

#Create a base class Bird, with a constructor and two methods. Then, create a child class that inherits the constructor from Class Bird and has two functions. Finally, display how you can use Super to access the parent class constructor inside the child class.