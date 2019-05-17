#Assining a new List slice
print('I want to change the coffee and apples and replace them with coke')
Cart[0:2]=['Coke'] #Can also be written Cart[:2]=Coke *Notice brackets
print(Cart)
#Pro Tip: if you want to delete every 2 entry del cart [::2]
#notice the double colon

#Deleting items from a list
del Cart[1]
print(Cart)
