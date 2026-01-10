inp = input("Enter a number:")


def disarium(inpList):
    output=0
    for i in range(len(inpList)):
        num = int(inpList[i])
        output=output+num**(i+1)1
    if str(output)==inp:
        print(inp,"is a disarium number")
    else:
        print(inp,"is not a disarium number")

disarium(inp)