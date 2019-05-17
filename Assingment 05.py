#Question 1, Even and odd number program
print('Hello friend, can you give me a number please?')
num =int(input('Please input number here: '))
mod =num%2
if mod ==0:
    print(num, 'Is an even number')
else:
    print(num, 'Is an odd number')

#Question 2
print('\nWelcome to Hogwarts!')
PW=input('Pleas enter the secret password here:')
if PW == 'secret':
    print('Great password!')
else:
    print('Password is bad, muggle!')

#Question 3
print('\nI can guess your mood if you enter a number!')
num=input('please enter a random number between 1 and 4 here: ')
if num == '1':
    print('Happy')
elif num == '2':
    print('okay')
elif num == '3':
    print('sad')
else:
    print()

#Question 4
print('\nI can do cool stuff with words.')
word= input('please enter a word here: ')
for letter in word:
    print(letter)
print('The word,',word,', is',len(word), 'letters.')
print('The first letter is:',word[0])
print('The second letter is:',word[1])
print('The third letter is:',word[2])
print('The fourth letter is:',word[3])

#Question 5
print('\n I can count stuff for you.')
start= int(input('enter the starting number here: '))
end= int(input('enter the ending number here: '))
by= int(input('enter by what increments I should count by here: '))
for i in range(start, end, by):
        print(i, end=', ')

#Question 6
Phrase=input('\nplease enter a short phrase here: ')
#Explanation for bracket code [begin : end : Sequence order]
print('Your phrase is:\"',Phrase, '\"\nIn reverse, that phrase is:','\"',Phrase[::-1],'\"')

