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
    
#Problem 2, Holiday shopping linst
List = []
Num=''
Gif=''
Nam=''
Amt=''

while Num != 0:
    Num=int(input('\nEnter a 0 to exit and show top 3 expensive gifts, \na 1 to show Holiday List or a 2 to add gift recipient: '))
    if Num == 1:
        print('\n',List)
    elif Num == 2:
        print('\nAdd to your List!')
        Nam=input('Enter the name here: ')
        Gif=input('Enter the gift here: ')
        Amt=int(input('Enter the price here (Whole number please): '))
        entry=(Amt, Gif, Nam)
        List.append(entry)
        List.sort(reverse=True)
        print('\n',List)
    else:
        print('Good-bye, here is a shor list of the top 3 most expensive items on your list:')

print(List[0:3])


