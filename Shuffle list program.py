#Problem 1 Homework 06, Shuffle a list program
import random
List=[1,2,3]
print('''This program will randomize list for the user.
First we will need some words, lets do a list of 3.''')
List[0]=input('Enter the first word in your list here: ')
List[1]=input('Enter the second here: ')
List[2]=input('Enter the third here: ')
print('\nGreat!, your list is:',List)
print('\nNow lets jumble things up a bit!')
input('Press enter to randomize the list.')
#Indexing the list
for i in range(len(List)):
    #Setting a random choice variable
      Rand = random.choice(List)
      #Printing that random choice
      print(Rand)
      #Removing the chosen value as an option (So there are no repeat values)
      List.remove(Rand)
