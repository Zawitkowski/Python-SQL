import scikitlearn

#Commonly used packages by data scientists

#Pandas / Pd / Pd.XxXxxx (using the pandas package)

#Scikitlearn --> Machine learning

#numpy --> math manipulation

#Practice
#print the letters in the word red, randomly 10 times
import random
Word = input('Word is:')
for i in range(10):
    position= random.randrange(-len(Word), len(Word))
    print(Word[position])
