dictionary1={"codingal":3,"is":2,"best":2,"for":2,"coding":1}
number=int(input("Enter a number:"))
frequency=0
for i in dictionary1:
    if (i.values)==number:
        frequency=frequency+1
print(number,"is in the dictionary",frequency,"times")