print("Hello, would like to play a game?")
input("press the enter key to continue")
print("\n Ok, lets play...")
Name=input("What is your name? : ")
Age= int(input('How old are you? : '))
Weight=int(input('how much do you weigh? : '))
print("\n", Name.upper(), Name.lower())
Calling= Name
print(Calling* 5)
print("Well then,"+ Name +"Your age in seconds is:", Age*60*60*24*365)
print("Your weight on the moon is:", Weight*0.165, "lbs")
print("your weight on the sun is:", Weight*9.8, "lbs")
        
print('\n do want to play an expense game?')
input('\tPress enter to continue')
print('If you want I can calculate your daily expenses')
print("Enter how much you spend per day on the following items:")
car= int(input('insurance:'))
bus= float(input('bus:'))
rent= float(input('my rent is:')) #The "float" allows me to use decimals!"
food= int(input('groceries and dining out:'))
shopping= int(input('my personal shopping:'))
total= car+bus+rent+food+shopping
print('And your grand daily total is:', total)

