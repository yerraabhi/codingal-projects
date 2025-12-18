#Write a program to create a class Parrot and perform the following tasks - Create a class variable species, Create a constructor that has instance variables - name and age, Create instances of class Parrot, passing arguments as well, Print Class variable by accessing it, Print Instance variables as well.

# class Parrot:
#     species="bird"

#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

# p1=Parrot("parro",2)
# p2=Parrot("parot",4)

# print("Parro is a {}".format(p1.species))
# print(p2.name,"is of",p2.age,"years of age")

# Write a Python class named Rectangle with a length and width and a method that computes the area of a rectangle. Display the dimensions and calculated area of the rectangle as well.

# class rectangle:
#     def __init__(self, l, w):
#         self.length=l
#         self.width=w

#     def rectangle_area(self):
#         return self.length*self.width

# newRectangle=rectangle(12,10)
# print("Dimension Of Rectangle - Length:%d Width:%d" % (newRectangle.length,newRectangle.width))
# print("Area Of Rectangle:", newRectangle.rectangle_area())

#Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
class circle:
    def __init__(self, radius):
        self.radius=radius
    
    def area(self):
        return 3.14159*self.radius*self.radius
    
    def perimeter(self):
        return 2*3.14159*self.radius
    

c=circle(10)
a=c.area()
p=c.perimeter()
print("Area is",a,"\nPerimeter is",p)