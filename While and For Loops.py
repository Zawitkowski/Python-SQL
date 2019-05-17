#While loop
word='kim'
letter1 =word[0]
letter3=word[2]
len(word)

print(letter1)
print(letter3)
print(len(word))

#While loop, what I did

'''words="star"
letter1=words[0]
letter2=words[1]
letter3=words[2]
letter4=words[3]

Response = ""
while index < len(words):
    Response= print(letter1)
    print(letter2)
    print(letter3)
    print(letter4)'''
#What I was supposed to do
word=input('Enter any word: ')
print("\n Here is each letter in your word: ")
index=0
while index<len(word):
    letter=word[index]
    print(letter)
input("\n\nPress enter to exit")

#The For Loop
word=input('Enter any word: ')
print("\n Here is each letter in your word: ")
for letter in word:
    print(letter)

input("\n\n\tPress Enter to EXIT")

