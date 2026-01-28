#Write a program to calculate the sum of whole numbers.
nums=int(input("Enter a number to calculate sum:"))
sum=0

for i in range(1, nums+1):
    sum=sum+i
    print("\nSum",sum)

#Write a program to reverse the string entered by the user.
string=input("Enter a string to reverse it: ")

stringreversed=("")

for i in string:
    stringreversed=i+stringreversed

print("Normal String:", string)
print("Reversed String:", stringreversed)

#Write a program to print the numbers in reverse order beginning from the number entered by the user.
num=int(input("Enter a number:"))

for i in range(num,0,-1):
    print(i)