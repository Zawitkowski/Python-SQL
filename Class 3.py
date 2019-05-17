print('In class practice 12/28/2019')
#Practice 1
print('practice 1')
print("Hello, would like to do a simulation?")
input("press the enter key to continue")
print("\n\t Ok, lets play...")
Name=input("\nWhat is your name? : ")
Age= int(input('How old are you? : '))
print("Well then, "+ Name +", the year when you turn 100 years old will be:", (2019-Age)+100)

#Practice 2
number= input('\n\tHey, how many years are in a century? \n answer here:')
if number== "100":
    print('\nCongrats, you are smart')
else :
    print('\nYou should know that...')
print('\n blah \n')

#Practice 3

number= input('Hey can you enter a random number under 100 please?')
if number >= "25":
    print('the number is 25')
else:
    print('This number is not under 25')

print('Practice 4')
Response=""
while Response != "32":
    Response= input("How old are you bro?")

#Practice 5
Day= input('What day of the week is it today?')
if Day == 'monday':
    print('Oh, that\'s the first day of the week!')
elif Day == 'tuesday':
          print('Oh, that\'s the second day of the week!')
elif Day == 'wednesday':
          print('Oh, that\'s the third day of the week!')
elif Day == 'thursday':
          print('Oh, that\'s the fourth day of the week!')
elif Day == 'friday':
          print('Oh, that\'s the fifth day of the week!')
elif Day == 'saturday':
          print('Oh, that\'s the sixth day of the week!')
elif Day == 'sunday':
          print('Oh, that\'s the last day of the week!')
else:
    print(Day, 'is not a day in the week')


