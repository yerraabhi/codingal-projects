#Overload the less than (<) and equal to (==) operators. For example, create objects - ob1 and ob2 with values 3 and 4 to compare values, respectively. You can additionally create more objects to try different values.

class A:
    def __init__(self,a):
        self.a=a
    
    def __lt__(self,other):
        if self.a < other.a:
            print("Obj1 is less than obj2")
        else:
            print("Obj2 is less than obj1")
    
    def __eq__(self, other):
        if(self.a < other.a):
            return "Both are equal"
        else:
            return "Not equal"

ob1=A(2)
ob2=A(3)

print("Passed values",ob1.a,ob2.a)
print(ob1 < ob2)

ob3=A(4)
ob4=A(4)

print("Passed values",ob3.a,ob4.a)
print(ob3 == ob4)

#reate a flashcard using object-oriented programming. A flashcard is a two-sided card with information on both sides that can assist memory. A question and an answer are usually printed on one side of a flashcard. Follow these steps to complete the activity - 1. From the user, take the input for a word and its definition. 2. To assign values for Word and Meaning, create a class called flashcard and use the __init__() function. 3. We'll use the __str__() function to get a string with the term and its definition. 4. Save the strings that have been returned in a list. 5. To print all of the stored flashcards, use a while loop.

class flashcard:
    def __init__(self,word,meaning):
        self.word=word
        self.meaning=meaning
    
    def __str__(self):
        return self.word+"("+self.meaning+")"

flash=[]
print("Welcome to flashcard applications")

while(True):
    word=input("Enter the name you want to add to flashcard:")
    meaning=input("Enter the meaning of tthe word:")

    flash.append(flashcard(word,meaning))
    option=int(input("Enter 0 if you want to add aother flashcard otherwise enter 1:"))

    if(option):
        break

print("\nYour flashcards")
for i in flash:
    print(">",i)