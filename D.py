Mydictionary={'Mill':'Tool used to cut through wood and steel', 'Drill':'Tool used to make holes',
              'Bore':'Tool used to make holes of precise diameters', 'Chamfer':'Cleaning // angle tool'}
print(Mydictionary['Mill'])
print(Mydictionary.get('Drill','I have not idea what that is'))
print(Mydictionary.get('Dril','I have not idea what that is'))
print(Mydictionary.keys())
print(Mydictionary.values())

#Problem 1 Homework 06, Shuffle a list program
List= [1,2,3,4,5,6,7,8,9]
import random
for i in range(len(List)):
    choice= random.choice(List)
    print(choice)
    List.remove(choice)
