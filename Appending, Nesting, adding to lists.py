nested = ['first', ('second', 'third'), ['fourth', 'fifth', 'sixth'] ]
print(nested)

Scores = [('Jane', 100), ('Diane', 120), ('Mike', 150), ('Alex', 100)]
print(Scores)

print(Scores[0])

print(Scores[0][1])

name, date, score = ("Jack","Monday", 145)
print(date)
print(name)
print(score)

Num=''
Nam=''

while Num != 0:
    Num=int(input('\nEnter a 0 to exit, a 1 to list Scores or a 2 to add score: '))
    if Num == 1:
        print('\n',Scores)
    elif Num == 2:
        print('\nAdd to your collection!')
        Scr=int(input('Enter your score here: '))
        Nam=input('Enter your name here: ')
        entry=(Nam, Scr)
        Scores.append(entry)
        Scores.sort(reverse=True)
        print('\n',Scores)
    else:
        print('Good-bye')
