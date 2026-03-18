T1=("ABC",)
print(type(T1))

#Perform the following operations: 1. Create a tuple with different datatypes 2. Create another tuple of integers 3. Create a new tuple by adding 9 to the previous tuple 4. Count the occurrences of an element in the tuple 5. Perform slicing on the tuple

tuple1=("a",2,9.7,"b",3.4,7)
tuple2=(1,2,34,6,7,3,97,34,7,1,97,1)
tuple3=(tuple2+(9,))
print(tuple2[4:9])
print(tuple2.count(1))
print(tuple3)

#Check whether the given tuple - (1,2,3,3,2,1) is a palindrome or not. If it's a palindrome, then it is the same after being reversed.
def palind(r):
    e=len(r)-1
    s=0
    while (s<e):
        if(r[s]!=r[e]):
            return False
        s+=1
        e-=1
    return True
r=(1,2,3,3,2,1)
if palind(r):
    print("The tuple is flip-flop")
else:
    print("The tuple is not flip-flop")