# Dev: Diala Ezzeddine
#Date: 3/4/2019
#Desc: Lists and Dictionaries



# someone’s cart
# Demonstrates lists creation

# create a list with some items and display with a for loop

cart = ["coffee", "orange", "tea" ,"chocolate"]
print("\nYour items:")
for item in cart :
     print(item)

input("\nPress Enter to continue.")

#get the length of a list
print("you have", len(cart), "items in your cart.")

input("\nPress Enter to continue.")

#test for membership using in
if "tea" in cart:
	print("you have the tea item in your cart")

input("\nPress Enter to continue.")

#display 1 item through an index
index = int(input("\nEnter the index number for an item in the cart:"))
print ("At index", index, "is", cart[index])

input("\nPress Enter to continue.")

#display a slice
start = int(input("\nEnter the index number to begin a slice:"))
finish= int(input("\nEnter the index number to end the slice:"))
print("cart[",start, ":", finish, "] is " , end="")
print(cart[start:finish])

input("\nPress Enter to continue.")

#concatenate 2 Lists
cart2 = [ "wipes","shampoo","soap"]
print("Your second cart contains:")
print(cart2)
print("let’s add the contents of the second cart to your first cart")
cart += cart2
print("your cart now is :")
print(cart)

input("\nPress Enter to continue.")


#Assign by index

print("I want to change the coffee for a yogurt")
cart[0] = "yogurt"
print ("your cart now is:")
print(cart)

input("\nPress Enter to continue.")

#Assign by slice
print("I want to change the yogurt and orange and replace them with coke")
cart[0:2] = ["Coke"]
print ("your cart now is:")
print(cart)

input("\nPress Enter to continue.")

#Delete an element
print("I want to remove the chocolate from my cart")
del cart[2]
print ("your cart now is:")
print(cart)

input("\nPress Enter to continue.")

#Delete a slice
print("I want to remove the first 2 items in my cart")
del cart[:2]
print ("your cart now is:")
print(cart)


input("\n\nPress Enter to exit.")



# high scores
# Demonstrates list methods

Scores = []
choice = None
while choice != "0":
    print(""" High Scores: 0= exit, 1= Show Scores, 2= Add a Score, 3= Delete a Score, 4= sort Scores""")
    choice = input("choice:")
    print(choice)
    #exit
    if choice == "0":
         print("good-bye.")
    #list high-score table
    elif choice =="1":
        print("High Scores")
        for item in Scores:
            print(item)
    #add a score
    elif choice =="2":
        score = int(input("what score did you get?:"))
        Scores.append(score)
        print(Scores)
    #remove a score
    elif choice =="3":
        score = int(input("Remove which score?:"))
        if score in Scores:
            Scores.remove(score)
            print(Scores)
        else:
            print(score,"isn’t in the high scores list.")
    #sort scores
    elif choice =="4" :
        Scores.sort(reverse= True)
        print(Scores)
    #some unkown choice
    else:
        print("Sorry, but", choice, "isn’t a valid choice.")
input("\n\nPress the enter key to exit")



#Nested sequence

nested = [ "first", ("second", "third"), ["fourth", "fifth", "sixth"] ]
print(nested)

Scores = [("Jane", 100), ("Diane", 120), ("Mike", 150), ("Alex", 100)]
print(Scores)

print(Scores[0])
print(Scores[1])
print(Scores[2])
print(Scores[3])


print(Scores[0][1])

# unpacking sequence
name, score = ("Jack", 145)
print(name)
print(score)

name, date, score = ("Jack","Monday", 145)
print(date)
print(name)
print(score)

#using the Nested sequences
Scores = []
choice = None
while choice != "0":
    print(""" High Scores with names of players: 0= exit, 1= Show Scores and names in the nested list, 2= Add a Score and name to the nested list """)
    choice = input("choice:")
    print()
    #exit
    if choice == "0":
         print("good-bye.")
    #display high-score table
    elif choice =="1":
        print("High Scores\n")
        print("Name\tScore")
        for entry in Scores:
            score, name = entry
            print(name,"\t", score)
    #add a new element (score, name), sort and keep the top 5 scores
    elif choice =="2":
        name = input("what is the player’s name?:")
        score = int(input("what score did the player get?:"))
        entry= (score, name)
        Scores.append(entry)
        Scores.sort(reverse=True)
        Scores = Scores[:5]
        print(Scores)
#some unknown choice
    else:
        print("Sorry, but", choice, "isn’t a valid choice.")
input("\n\nPress the enter key to exit")

#######################Dictionaries####################################

Mydictionary = {"googling": "searching the internet for information","tweeting": "posting message on Twitter", "like": "share that you are in favor of a post on Facebook"}
print(Mydictionary)


#Using a key to retrieve a value
print(Mydictionary ["googling"])
#Testing for a key with the in operator before retrieving a value
if "googling" in Mydictionary:
     print (" I know what googling means:")
     print(Mydictionary ["googling"])
else:
     print("I have no idea what googling means")


#Using the get() method to retrieve a value:
print(Mydictionary.get ("googling"))

#If the key doesn’t exist in the dictionary, get() method returns a default value which we can define, like the following:
print(Mydictionary.get ("googling", "I have no idea"))

print(Mydictionary.get ("texting"))
print(Mydictionary.get ("texting","I have no Idea"))


# Special term translator
# Demonstrates using dictionaries


Mydictionary = {"googling": "searching the internet for information","tweeting": "posting message on Twitter", "like": "share that you are in favor of a post on Facebook"}
choice = None
while choice != "0" :
    print("""
	 Mydictionary term
	 0= quit
	 1= look up for a term in Mydictionary
	 2= Add a term to Mydictionary
	 3= Redefine a Mydictionary term
	 4= Delete a Mydictionary term
	""" )
    choice = input("your choice:")
    print()
    #exit
    if choice =="0":
        print("good-bye")
    #get a definition
    elif choice=="1":
        term = input("what do you want me to translate:")
        if term in Mydictionary:
            definition = Mydictionary[term]
            print("\n", term, "means", definition)
        else:
            print("\nSorry, I don’t know this", term)
    #add a term-definition pair
    elif choice =="2":
        term = input("what term you want to add?:")
        if term not in Mydictionary:
            definition = input("what is the definition?:")
            Mydictionary[term] = definition
            print("\n", term, "has been added")
        else:
            print("\nThat term already exist!try redefining it")
    # redefine an existing term
    elif choice =="3":
        term = input("what term you want to redefine?:")
        if term in Mydictionary:
            definition = input("what is the new definition?:")
            Mydictionary[term] = definition
            print("\n", term, "has been redefined")
        else:
            print("\nThat term doesn’t exist! try adding it")
    #delete a term-definition pair
    elif choice =="4":
        term = input("what term you want to delete?:")
        if term in Mydictionary:
            del Mydictionary[term]
            print("\nOkay, I deleted ", term)
        else:
            print("\nI can’t do that!", term, "doesn’t exist in the dictionary")
    # some unknown choice
    else:
        print("\nSorry your choice isn’t valid")
input("\n\nPress the enter key to exit.")


Mydictionary = {"googling": "searching the internet for information","tweeting": "posting message on Twitter", "like": "share that you are in favor of a post on Facebook"}
print(Mydictionary.keys())

print(Mydictionary.values())

print(Mydictionary.items())


#practice 
MothersName = {"Jane": "Julia", "Harry": "Princess Diana","bob": "vicky", "John": "camille"}
choice = None
while choice != "0" :
    print("""
	 MothersName dictionary of person-mother
	 0= quit
	 1= look up for a person's mother name in MothersName dictionary
	 2= Add a person-mother to MothersName dictionary
	 3= Redefine a MothersName dictionary person-mother
	 4= Delete a MothersName dictionary person-mother
	""" )
    choice = input("your choice:")
    print()
    #exit
    if choice =="0":
        print("good-bye")
    #get a person's mother name
    elif choice=="1":
        person = input("who is the person:")
        if person in MothersName:
            mother = MothersName[person]
            print("\nThe", person, "mother name is ", mother)
        else:
            print("\nSorry, I don’t know this", person)
    #Add a person-mother pair
    elif choice =="2":
        person = input("who is the person that you want me to add:")
        if person not in MothersName:
            mother = input("what is the mother's name?:")
            MothersName[person] = mother
            print("\n", person, " mother's name has been added")
        else:
            print("\nThat person mother's name already exist! try to replace it")
    # replace an existing pair
    elif choice =="3":
        person = input("what person's mother name you want to replace?:")
        if person in MothersName:
            mother = input("what is the new definition?:")
            MothersName[person] = mother
            print("\n", person, "has been replaced")
        else:
            print("\nThat person doesn’t exist! try adding it")
    #delete a person-mother pair
    elif choice =="4":
        person = input("what person you want to delete?:")
        if person in MothersName:
            del MothersName[person]
            print("\nOkay, I deleted ", person)
        else:
            print("\nI can’t do that!", person, "doesn’t exist in the dictionary")
    # some unknown choice
    else:
        print("\nSorry your choice isn’t valid")
input("\n\nPress the enter key to exit.")

