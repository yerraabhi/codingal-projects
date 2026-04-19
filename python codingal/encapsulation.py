#Create a class with following variables and methods - 1. Private variable named privateVar that contains an integer value 2. Create a private function privMeth that prints a message 3. Create a function hello that prints the value of privateVar 4. Create an object for the class and call all the functions.

class myclass:
    __privatevar=27

    def __privmeth(self):
        print("I am inside class myclass")
    
    def hello(self):
        print("Private Variable Value:",myclass.__privatevar)

foo=myclass()
foo.hello()
foo.__privmeth

#Create a class Point that consists of a constructor to set coordinates equal to x and y. Also, it consists of a function that returns the coordinates in Point format. Create an object passing the coordinates and print the Point.

class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)

p1=Point(2,3)
print(p1)