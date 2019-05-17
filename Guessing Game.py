#This is a Guessing game
words=['soccer','golf','football','basketball','lacrosse']
print('These are the words you may guess',words)
import random
for i in range(1):
    pick=words[random.randint(0,4)]
print('There are',len(pick),'letters in this word')

letters= pick[0:len(pick)]
count=0
limit=5
while count<limit:
    let=input('guess a single letter in the word:')
    if let in pick:
        print('Yes')
        count +=1
    else:
        print('no')
        count +=1

print('\nYou are not allowed anymore hints')
input('press enter to continue')
print('Now you must guess the word')

guess= input('Your best guess here: ')
if guess == pick:
    print('Good job, you are smart!')
else:
    print('Sorry, the correct word was:',pick)
    
