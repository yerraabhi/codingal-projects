#Check alphabet “A” is present in the given string or not. And terminate the loop after finding the alphabet “A”

# string=input("Enter a string:")
# for i in string:
#     if i=="A":
#         print("A is found")
#         break
#     else:
#         print("A not found")

#Satisfy the following conditions of the given range: If the number is divisible by 20, it provides an output "twist." If the number is divisible by 15, it will pass (no output) If the number is divisible by 5, it will give an output “fizz.” If the number is divisible by 3, it will give an output "buzz." Otherwise, it will give the output of that number

# for i in range(20):
#     if i%20==0:
#         print("twist")
#     elif i%15==0:
#         pass
#     elif i%5==0:
#         print("fizz")
#     elif i%3==0:
#         print("buzz")
#     else:
#         print(i)

#Display 1 to 10 numbers in reverse order and skip the number 5
for i in range(10,0,-1):
    if i==5:
        continue
    print(i)