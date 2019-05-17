print('Hi dude, can ask you something personal?')
word=input('Relax, I just want you to type in your favorite word here: ')

#Notice how the "in" operator is used with the "if" statement.
print('\nDude you word is', len(word), 'letters long. Ha ha, rad.')
if 'e' in word:
    print('Whoa, there is an e in that word bro!')
else:
    print('Dude, no e\'s in that word, lame sauce...')
import random
word=input('Put word here: ')

for i in range(0,10):
    print(word[random.randrange(len(word))])

#Using the while loop for this problem
word=input('word is: ')
outcome=0
while outcome<10:
    letter=word[random.randrange(len(word))]
    print(letter)
    outcome+=1

#What the teacher did
word=str(input("Give a word: "))
high=len(word)
low=-len(word)
for i in range(10):
    position= random.randrange(low,high)
    print('word[',position,']\t',word[position])

#How I was trying to do it before
#Notce "len(word)-1" because the first letter of the word is indexed at 0
word=input('Type word here')
for i in range(10):
    rnd= random.randint(-len(word),len(word)-1)
    print('word[',rnd,']:', word[rnd])
