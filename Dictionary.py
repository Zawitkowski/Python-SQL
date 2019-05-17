# Special term translator
# Demonstrates using dictionaries
Mydictionary = {"googling": "searching the internet for 
information","tweeting": "posting message on Twitter", "like": "share that 
you are in favor of a post on Facebook"}
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
print("\nI can’t do that!", term, "doesn’t exist in the 
dictionary")
# some unknown choice
else:
print("\nSorry your choice isn’t valid")
input("\n\nPress the enter key to exit.")
