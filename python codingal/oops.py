#Write a program to create a class Parrot and perform the following tasks - Create a class variable species, Create a constructor that has instance variables - name and age, Create instances of class Parrot, passing arguments as well, Print Class variable by accessing it, Print Instance variables as well.

class Parrot:
    species="bird"

    def __init__(self,name,age):
        self.name=name
        self.age=age

p1=Parrot("parro",2)
p2=Parrot("parot",4)

print("Parro is a {}".format(p1.species))
print(p2.name,"is of",p2.age,"years of age")