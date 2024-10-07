""""
TUDAYAN, MARIA GRACIELLE G.
PYTHON ACTIVITY THAT PRINTS OUT INFO
"""

Fname = "Maria Gracielle"
Mname = "Garingo"
Lname = "Tudayan"
address = "Galimuyod"
age = 20
FavNumOne = 26
FavNumTwo = 30

print(Fname, Mname, Lname)

print(Fname)
print(Mname)
print(Lname)
print(address)
print(age)
print(FavNumOne)
print(FavNumTwo)

#store a arrays of animals
animals = ["butterfly", "Shark", "Lion"]
print(animals[1]) #print the result which is "Shark"

ActorOne = "Ang gwapo gwapo ko diba? friend 'MAkMak'"
ActorTwo = 'Thankyou! "Macayan Puyot"'
print(ActorOne)
print(ActorTwo)
print(ActorOne[5]) #it prints out the letter from the ActorOne which is "w"

#it will get the characther lengt stored in ActorOne, ActorTwo, and my Addres
actor_oneL  = len(ActorOne) 
actor_twoL = len(ActorTwo) 
addressL = len(address) 

#prints out the result
print(actor_oneL)
print(actor_twoL)

#in this part, it will add the character length of ActorOne and ActorTwo, after that it will subtruct to the character length of myy address
results = (actor_oneL + actor_twoL) - addressL
print(results) #print the result which is 40+25=65-9=56