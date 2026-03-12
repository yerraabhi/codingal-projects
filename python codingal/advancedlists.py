#Count the number of strings where the string length is two or more, and the first and last characters are the same from a given list of strings.

# def matchwords(words):
#     ctr=0
#     lst=[]
#     for word in words:
#         if len(word)>1 and word[0]==word[-1]:
#             ctr+=1
#             lst.append(word)
#     print("List of words with first and last charater same\n",lst)
#     return ctr

# count=matchwords(["abc","cfc","xyz","aba","1221"])
# print("Number of words with first and last charater same:",count)

#Find the sum and average of the list. The average of the list is defined as the sum of the elements divided by the number of the elements. Also, find the largest and the smallest number in the list.

L=[12,3,5,4,52,6,2,7]
print("Original List:",L)

count=0

for i in L:
    count+=i

avg=count/len(L)

print("Sum=",count)
print("Average=",avg)

print("Maximum=",max(L))
print("Minimum=",min(L))