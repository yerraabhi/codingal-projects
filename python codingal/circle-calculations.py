class circle:
    def __init__(self, radius):
        self.radius=radius
    
    def area(self):
        return 3.14159*self.radius*self.radius
    
    def perimeter(self):
        return 2*3.14159*self.radius
    
r=int(input("Enter circle radius:"))
c=circle(r)
a=c.area()
p=c.perimeter()
print("Area is",a)
print("Perimeter is",p)