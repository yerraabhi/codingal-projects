#check how many times a character is repeated in a word?
string=input("Enter a word:")
char=input("Enter a character:")
i=0
count=0

while (i<len(string)):
    if(string[i]==char):
        count=count+1
    i=i+1

print(char,"has occurred",count,"times in this word.")

#Write a program to print all the prime numbers which come in the range entered by the user?
lower=int(input("Enter a lower range:"))
upper=int(input("Enter a upper range:"))
print("Prime numbers beetween",lower,"and",upper,"are:")

for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                break
        else:
            print(num)