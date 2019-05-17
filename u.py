#Replacing items in a list
'''Cart=['coffee','orange','tea','chocolate']
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
print(Cart)'''
    
#refer All Together slide in canvas
score=[]
choice=''
while choice !=0 :
   print('0 = exit, 1= show scores, 2= add a score, 3= delete a score and 4 sort scores')
   choice=int(input('pick a number here'))
   if choice == 0:
       print('thank you')
   else:
       print('That is not a valid choice')
