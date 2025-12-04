#Write a Python program to first take a number as an input from the user, then check whether that number is positive, negative, or neutral (if equal to zero) and print the result.

num=int(input("Enter a number:"))
if num>0:
    print(num , "is positive")
elif num<0:
    print(num , "is negative")
elif num==0:
    print(num , "is neutral")
else:
    print("Invalid Input")

#Write a Python program to first take a number as an input from the user, then check whether that number is even or odd and print the result.

num=int(input("Enter a number:"))
if num%2==0:
    print(num , "is even")
else:
    print(num , "is odd")