class dog:
    animal="dog"
    def __init__(self,breed,colour):
        self.breed=breed
        self.colour=colour

dog1=dog("Golden Retriever","gold")
dog2=dog("Dalmatian","white and dark brown")

print(dog1.breed+" is "+dog1.colour)
print(dog2.breed+" is "+dog2.colour)