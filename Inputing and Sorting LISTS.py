'''#Replacing items in a list
Cart=['coffee','orange','tea','chocolate']
print('Your Cart contains:')
for i in Cart:
    print(i)

print('\nBut mommy I wanted Apples not oranges!')
print('Ok. *Waves magic wand')
Cart[1]='Apples'
print('\nPresto Chango! our cart now contains:')
for i in Cart:
    print(i)

#Assining a new List slice
print('I want to change the coffee and apples and replace them with coke')
Cart[0:2]=['Coke'] #Can also be written Cart[:2]=Coke *Notice brackets
print(Cart)
#Pro Tip: if you want to delete every 2 entry del cart [::2]
#notice the double colon

#Deleting items from a list
del Cart[1]
print(Cart)
    
#refer All Together slide in canvas
score=[]
choice=''
while choice !=0 :
   print('0 = exit, 1= show scores, 2= add a score, 3= delete a score and 4 sort scores')
   choice=int(input('pick a number here'))
   if choice == 0:
       print('thank you')
   else:
       print('That is not a valid choice')'''
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
      else:print(score,"isn’t in the high scores list.")
      #sort scores
   elif choice =="4" :
      Scores.sort(reverse= True)
      print(Scores)
      #some unkownchoice
   else:
      print("Sorry, but", choice, "isn’t a valid choice.")
input("\n\nPressthe enter key to exit")


























