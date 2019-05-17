# Dev: Diala Ezzeddine
#Date: 2/26/2019
#Desc: if, elif and While loop using Python

# Demonstrates random number generation
import random

# Generate random numbers from 1 to 10
#random.seed(123)
outcome1 = random.randint(1,10)
outcome2 = random.randrange(10) +1
print(outcome1)
print(outcome2)

Total = outcome1 + outcome2
print("The first random number is ", outcome1, "and the second is", outcome2, ". The total is ", Total )

# Demonstrate the use of if statement
print("Welcome to our class security system")
Password = input("Enter your password to get access to the classroom: ")
if Password =="BUAN4210" :
    print("Access Granted")

input("\n\nPress Enter to exit.")

# if statement comparing numeric 
Password = int(input("Enter a number: "))
if Password == 10 :
    print("correct number")
    print("\n Welcome")

input("\n\nPress Enter to exit.")

# Demonstrate the use of if statement with else clause

print("Welcome to our class security system")
Password = input("Enter your password to get access to the classroom: ")
if Password =="BUAN4210" :
    print("Access Granted")
else:
    print("Access Denied")


input("\n\nPress Enter to exit.")


# Demonstrates the use of elif clause

print("What is your score?")

# Generate random numbers from 1 to 5
score= random.randint(1,5)

if score == 5 :
    print("5. Excellent! Congratulations!")
elif  score ==4:
    print("4. Great Job!")
elif  score ==3:
    print("3. You can do better")
elif  score ==2:
    print("2. You need to study")
elif  score ==1:
    print("1. Drop your class")
else:
    print("This is not a score")


input("\n\nPress Enter to exit.")

# Demonstrates the while loop

Response = ""
while Response != "my name" :
    Response = input("What is your name?\n")

print("Oh. Okay")

input("\n\nPress Enter to exit.")

