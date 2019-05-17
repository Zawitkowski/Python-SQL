msg=input('Enter a message here:')
print(msg)
New_msg=""
vowels="aeiou"
for letter in msg:
    if letter.lower() not in vowels:
#What is happening her is illustrated through the print line within the loop.
        New_msg += letter
        print('a new string has been created: ', New_msg)
print('\n This is your old message without vowels,', New_msg)

