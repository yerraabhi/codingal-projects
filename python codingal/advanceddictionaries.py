#Create a dictionary that consists of - id, name, class and subject integration of students. Then, write a program to retrieve unique entries and eliminate the rest.
# studentdata={"id1":{"name":"Sara","class":"V","subjectintegration":"english,math,science"},"id2":{"name":"David","class":"V","subjectintegration":"english,math,science"},
# "id3":{"name":"Sara","class":"V","subjectintegration":"english,math,science"},
# "id4":{"name":"Surya","class":"V","subjectintegration":"english,math,science"}}

# result={}
# seenkeys=[]

# for studentid, details in studentdata.items():
#     uniquekey=(details["name"],details["class"],details["subjectintegration"])

#     if uniquekey not in seenkeys:
#         seenkeys.append(uniquekey)
#         result[studentid]=details

# for k,v in result.items():
#     print(k,":",v)

#Check the frequency of a value in a dictionary - {'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}.

# testdict={"codingal":2,"is":2,"best":2,"for":2,"coding":1}
# print("The original dictionary:" + str(testdict))

# K=2

# res=0
# for key in testdict:
#     if testdict[key]==K:
#         res=res+1

# print("Frequency of K is:"+str(res))

#Return the country code for various countries. Here’s a dictionary of different country codes - {'India' : '0091', 'Australia' : '0025', 'Nepal' : '00977'}.

countrycodes={'India' : '0091', 'Australia' : '0025', 'Nepal' : '00977'}
print("Country code for India-")
print(countrycodes.get("India","Not Found"))

print("Country code for Japan-")
print(countrycodes.get("Japan","Not Found"))