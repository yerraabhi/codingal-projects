for i in range(6):
    for i in range(1,i+1):
        print("*",end="")
    print()

#Write a program to find out the denominations of notes of 2000, 500, 200, 100, 50, 20, and 10 for the total amount of money entered by the user.

totalamount=int(input("Enter your total amount:"))
listofnotes=[500,200,100,50,20,10]
for i in listofnotes:
    numberofnotes=totalamount // i
    totalamount %= i
    if numberofnotes != 0:
        print(f"The number of notes of {i} is {numberofnotes}")

#WAP count the number of even and odd numbers from a tlist - [75,23,52,96,11,16,34,25,80]

numberlist=[75,23,52,96,11,16,34,25,80]
even=[]
odd=[]
for i in numberlist:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("even values=",even)
print("odd values=",odd)