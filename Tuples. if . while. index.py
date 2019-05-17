# Dev: Diala Ezzeddine
#Date: 2/26/2019
#Desc: While and for loops, strings and Tuples using Python

import random

# Demonstrates the while loop with a string
word = input("Enter any word: ")
print("\nHere’s each letter in your word: ")
index = 0
while index < len(word):
    letter = word[index]
    print(letter)
    index +=1
input("\n\nPress Enter to exit.")

# Demonstrates the For loop with a string

word = input("Enter any word: ")
print("\nHere’s each letter in your word: ")
for letter in word:
    print(letter)
input("\n\nPress Enter to exit.")



# Demonstrates the range() function

# counting number from 0 to 9
print("Counting: ")
for i in range(10):
    print(i, end= " ")

# counting all numbers of fives from 0 to 49 
print("\n\nCounting by fives: ")
for i in range(0, 50, 5):
    print(i, end= " ")

# counting all numbers backwards from 10 to 1
print("\n\nCounting backwards: ")
for i in range(10, 0, -1):
    print(i, end= " ")

input("\n\nPress Enter to exit.")

# Other For loop usage:

# print Hi 10 times
for i in range(10):
    print("Hi!")
    
# print Hi 10 times separated by ,
for i in range(10):
    print("Hi!", end = ", ")

input("\n\nPress Enter to exit.")

#################Strings###################

#Demonstrates the len() function and the in operator
message = input("Enter a message: ")
print("\nThe length of your message is:" , len(message))
print("\nThe most common letter in the English language, 'e', ")
if "e" in message:
    print("is in your message.")
else:
    print("is not in your message")

input("\n\nPress Enter to exit.")


#Demonstrates string indexing

word = str(input("Give me a word:"))
print("The word is:" , word, "\n")
high = len(word)
low = -len(word)
for i in range(10):
	position = random.randrange(low,high)
	print("word[", position, "]\t", word[position])

input("\n\nPress Enter to exit.")

# string are immutable
name = "John"
print(name)
name = "chris"
print(name)

Word = "game"
#Word[0] = "l"



# Demonstrates creating new strings with a For loop

message = input("Enter a message: ")
new_message = ""
vowels = "aeiou"
for letter in message:
    if letter.lower() not in vowels:
        new_message += letter
        print("a new string has been created:" , new_message)
print("\nYour message without vowel is :", new_message)

input("\n\nPress Enter to exit.")

# Demonstrates string slicing

word = "cake"
print("Enter your beginning and ending index for slicing your cake:")
print("Press the enter key at ‘Start’ to exit.")
start = None
while start != "":
    start = input("\nStart")
    if start:
	    start= int(start)
	    finish = int(input("Finish"))
	    print("word[",start, ":", finish, "] is " , end=" ")
	    print(word[start:finish])

input("\n\nPress Enter to exit.")

#################Tuples###################

# Someone’s cart
# Demonstrates tuple creation

# Create an empty tuple
cart = ()

# treat the tuple as a condition
if not cart :
  print("your cart is empty.")

input("\nPress Enter to continue.")

# create a tuple with some items

cart = ("coffee", 
              "orange",
                "tea",
                "chocolate")

#print the tuple
print("\nThe tuple cart is :")
print (cart)

#print each element in the tuple
print("\nYour items:")
for item in cart :
     print(item)
# length of a tuple     
print("you have", len(cart), "items in your cart.")

#test for membership using in

if "tea" in cart:
	print("you have the tea item in your cart")

#display 1 item through an index

index = int(input("\nEnter the index number for an item in the cart:"))
print ("At index", index, "is " , cart[index])

#display a slice

start = int(input("\nEnter the index number to begin a slice:"))
finish= int(input("\nEnter the index number to end the slice:"))
print("cart[",start, ":", finish, "] is " , end=" ")
print(cart[start:finish])


#concatenate 2 tuples

cart2 = ( "wipes",
         "shampoo",
         "soap")
print("Your second cart contains:")
print(cart2)
print("let’s add the contents of the second cart to your first cart")
cart += cart2
print("your cart now is :")
print(cart)


input("\n\nPress Enter to exit.")


