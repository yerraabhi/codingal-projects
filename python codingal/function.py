# name=input("Enter your name:")
# def wellwishes(name):
#     print("Hello how are you",name)

# wellwishes(name)

#Make a calculator : For making a calculator create four functions add, subtract, multiply, divide. Ask for a choice from users which operation they want to perform. Take user input whatever operation they want to perform And call that function accordingly.

def addition(num1,num2):
    return num1+num2

def subtraction(num1,num2):
    return num1-num2

def multiplication(num1,num2):
    return num1*num2

def division(num1,num2):
    return num1/num2

print("Select Operation:\nA For Addition\nB For Subtraction\nC For Multiplication\nD For Division")

choice=input("Enter Choice(A/B/C/D):")
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))

if choice=="A":
    print(num1,"+",num2,"=",addition(num1,num2))
elif choice=="B":
    print(num1,"-",num2,"=",subtraction(num1,num2))
elif choice=="C":
    print(num1,"x",num2,"=",multiplication(num1,num2))
else:
    print(num1,"/",num2,"=",division(num1,num2))