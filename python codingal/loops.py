# #Write a Python program for printing the table (1 to 10), using for loop.
# num=int(input("Enter the number whose table you want  to display :"))
# for i in range(1,11):
#     print(num, "x", i, "=", num*i)

#Write a Python program for printing the sum of the first ten natural numbers using the while loop.
# sum=0
# for i in range(1,11):
#     sum=sum+i

# print("The sum or the first ten natural numbers is", sum)

# sum=0
# num=1
# while (num<=10):
#     sum=sum+num
#     num=num+1

# print("The sum or the first ten natural numbers is", sum)

#Write a Python program to take a number as input from the user and check whether it is a prime number or not.

num=29
flag= False
if num>1:
    #check for factors
    for i in range(2, num):
        if(num % i) == 0:
            flag=True
            break

if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")