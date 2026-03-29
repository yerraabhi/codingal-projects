#Create a set and perform the following operations on that set- 1. Create a set with integer elements 2. Create a set with mixed data type elements 3. Create another set with elements - 1, 2, 3, 4, 3, 2 4. Create a set from a list with elements - [1, 2, 3, 2] 5. Print the set after removing the first element from this set - [0, 1, 3, 4, 5]

# set1={1,3,4,2,6,33,7,3,66,34,7,4}
# set2={1,"a",25.5,2,"B",25.6}
# set3={1,2,3,4,3,2}
# list1=[1,2,3,2]
# set4=set(list1)
# set5={0,1,3,4,5}
# print(set1)
# print(set2)
# print(set3)
# print(set4)
# print(set5.pop())

#Find the intersection of two sets. Set1 = {green, blue} Set2 = {blue, yellow}

# set1={"green","blue"}
# set2={"blue","yellow"}
# print(set1.intersection(set2))

#Create an array with the following elements - [1, 3, 5, 3, 7, 9, 3]. Then find the number of occurrences of number 3 in the array. Also, print the reversed array.

import array as arr
array_num=arr.array("i",[1,3,5,3,7,9,3])

print("Original array:"+str(array_num))
print("Number of occurrences of the number 3 in the array:"+str(array_num.count(3)))

array_num.reverse()
print("Reversed array:")
print(str(array_num))