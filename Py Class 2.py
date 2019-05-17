import random
outcome1=random.randint(1,10)
outcome2=random.randrange(10)+1
Total = outcome1+outcome2
print('The first random number is',outcome1, ', and the second is', outcome2,'.The total is:',Total)
print('\n\t Printing the \"if\" statement')

Password = input("Welcome to Hogwarts! Who was nearly headless?:")
if Password == "Nick" :
    print('\n\n\t\t\tEllo Hamora!')
else:
    print('GO BACK TO SLITHERIN MALFOY!')

input("\n\n Press enter to exit")

Age = int(input('How old are you:'))
Cash = int(input('How much money do you have in your pocket?'))
if Age > Cash:
    print('Damn you broke!')
else:
    print('Let me borrow 12 dollars foo')


score= random.randint(1,5)

if score == 5:
    print("5. Excellent! Congratulations!")
elif score ==4:
    print("4. Great Job!")
elif score ==3:
    print("3. That's average.")
elif score ==2:
    print('2. You need to study')
elif score ==1:
    print('1. Get the hell out of my class')
else:
    print('This is not a score')

Response=""
while Response != "Adam":
    Response= input("What is your name?\n\t")

print("Oh. Okay...")
          



