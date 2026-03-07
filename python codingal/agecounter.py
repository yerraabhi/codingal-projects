try:
    age=int(input("Enter your age:"))
except ValueError:
    print("The age should be an integer")
else:
    print("The age is",age)