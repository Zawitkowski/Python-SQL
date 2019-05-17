# Question 6, 7, check for indentations!, q 50
Mydictionary = {}
choice = ''
while choice != 0 :
    choice = int(input("your choice:"))
    print("""
 Mydictionary term
 0: quit
 1; look something up
 2: Add a term 
 3: Redefine term
 4: Delete 
""" )

if choice =="0":
    print("good bye")

elif choice=="1":
    term = input("What shoudl I look up?:")
    if term in Mydictionary:
        definition = Mydictionary[term]
        print(definition)
    else:
        print("invalid entry")

elif choice =="2":
    print(Mydictionary.keys())
    term = input("what term you want to add?:")
    if term not in Mydictionary:
        definition = input("what is the definition?:")
        Mydictionary[term] = definition
        print(Mydictionary)
    else:
        print("\nThat term already exist!try redefining it")

elif choice =="3":
    term = input("what term you want to redefine?:")
    if term in Mydictionary:
        definition = input("what is the new definition?:")
        Mydictionary[term] = definition
        print("\n", term, "has been redefined")
    else:
        print("\nThat term doesn’t exist! try adding it")

elif choice =="4":
    term = input("what term you want to delete?:")
    if term in Mydictionary:
        del Mydictionary[term]
        print(Mydictionary.keys())

    else:
        print('Invalid entry')
