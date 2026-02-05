#Write a program to demonstrate a right angle triangle pattern?
# print("Half Pyramid Pattern Of Stars (*)")
# n=int(input("Enter the number of rows:"))
# for i in range(n):
#     for j in range(i+1):
#         print("*",end="")
#     print()

#Write a program to demonstrate a Floyd triangle pattern?
# rows=int(input("Enter the number of rows:"))
# number=1
# print("Floyd's Triangle")
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print(number,end=" ")
#         number=number+1
#     print()

#Write a program to demonstrate the numbers in a diamond pattern?
rowsize=int(input("Enter Rows:"))
if rowsize%2==0:
    halfdiamrow=int(rowsize/2)
else:
    halfdiamrow=int(rowsize/2)+1
space=halfdiamrow-1
for i in range(1,halfdiamrow+1):
    for j in range(1,space+1):
        print(end=" ")
    space=space-1
    num=1
    for j in range(2*i-1):
        print(end=str(num))
        num=num+1
    print()
space=1
for i in range(1,halfdiamrow):
    for j in range(1,space+1):
        print(end=" ")
    space=space+1
    num=1
    for j  in range(1,2*(halfdiamrow-1)):
        print(end=str(num))
    num=num+1
print()