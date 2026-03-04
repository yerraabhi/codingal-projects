# try:
#     number=int(input("Enter a number:"))
#     print("The number entered is",number)
# except ValueError as ex:
#     print("Exeption:",ex)

#Check how the exceptions and finally statement works

# try:
#     num1,num2=eval(input("Enter two numbers seperated by a comma:"))
#     result=num1/num2
#     print("The result is",result)
# except ZeroDivisionError:
#     print("Division by zero is error")
# except SyntaxError:
#     print("Comma is missing.Enter numbers like this 1,2")
# except:
#     print("Wrong input")
# else:
#     print("No exeptions")
# finally:
#     print("This code will always execute")

#Use nested while loop. If the value is divided by two, then it will run an infinite loop of the bye.

valid=False
while not valid:
    try:
        n=int(input("Enter a number:"))
        while n%2==0:
            print("bye")
            valid=True
    except ValueError:
        print("Invalid")