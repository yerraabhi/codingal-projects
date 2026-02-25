#Create a function total_calc() that helps us calculate and print out the total amount paid at a restaurant. Given a bill amount and the percentage of the bill amount you decide to pay us a tip (tip_perc ), this function calculates the total amount you should pay.

# def totalcalc(bill,tipperc):
#     total=bill*(1+0.01*tipperc)
#     print("The total bill is",total)

# bill=int(input("Enter amount of bill money:"))
# tipperc=int(input("Enter amount of percent of tip money:"))

# totalcalc(bill,tipperc)

#Define a function to find a cube and define another function which let execute the cube function if the number is divisible by 3

# def cube(number):
#     return number**3

# def bythree(number):
#     if number%3==0:
#         return cube(number)
#     else:
#         return False

# print (bythree(9))
# print (bythree(4))

#Find the factorial using recursive function

def factorial(x):
    """This is a recursive function to find the factorial of an integer"""

    if x==0 or x==1:
        return 1
    else:
        return x*factorial(x-1)

print(factorial.__doc__)
print("The factorial of 1=",factorial(1))
print("The factorial of 2=",factorial(2))
print("The factorial of 5=",factorial(5))
print("The factorial of 10=",factorial(10))
print("The factorial of 19=",factorial(19))