#When you turn 80 program 1
print("Hello, would like to do a simulation?")
input("press the enter key to continue")
print("\n\t Ok, lets play...")
Name=input("\nWhat is your name? : ")
Age= int(input('How old are you? : '))
print("Well then, "+ Name +", the year when you turn 100 years old will be:", (2019-Age)+100)

# 2, Little star
print('\nWant to hear me sing a song?')
input('press enter key to continue')
print('Twinkle, twinkle, little star,')
print('\tHow I wonder what you are!')
print('\t\tup above the world so high,')
print('\t\tlike a diamond in the sky.')
print('Twinkle, twinkle, little star,')
print('\tHow I wonder what you are!')

# 3, Circle
        
from math import pi
r = float(input ("\nInput the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))

# 4, Multi line string
print("""\nThis
is a ......multi-line
document string ------> example""")


# 5, First and Last name
FirstName=input("\nWhat is your first name? : ")
LastName=input("\nWhat is your last name? : ")
print(LastName, FirstName) 
