#Someone's Cart
#Demonstrates tuple creation

#Creat empty tuple
cart=()

#Treat the tuple as part of a condition
if not cart:
    print("Your cart is empty.")
input("\n press enter to put stuff in your cart")

#Creat tuple with some items
cart=('coffee',
      'orange',
      'tea',
      'chocolate')

#print the tuple
print('\nThe tuple cart now contains:')
print(cart)
input("\n\n Press Enter to exit")

print(len(cart))

print(cart[0], cart[1], cart[2], cart[3])

#Slicing tuples (works for word inexes as well)
input('press enter to slice [0:2]')
print(cart[0:2])
input('\n press enter to slice [1:3]')
print(cart[1:3])

#Concatenating tuples
#Define Second tuple
Basket=()
if not Basket:
    print ('\nyour basket is empty')
    input('press enter')
Basket=('Coffee Filters',
        'Juicer',
        'Hot water',
        'Milk')
print('\nThe basket contains', Basket)
print('\nWould you like to empy your basket into the cart?')
input('\nPress enter to continue')
Cart_Basket=(cart+Basket)
print('\n...dump, \t...dump, \t...dump')
print('\nYour cart now contains all of the following.')
print(Cart_Basket)
Basket[1]=='yogurt'
print(Basket)



