Scores = []
choice = None
while choice != "0":
   print(""" High Scores: 0= exit, 1= Show Scores, 2= Add a Score, 3= Delete a Score, 4= sort Scores""")
   choice = input("choice:")
   print(choice)
   #exit
   if choice == "0":
      print("good-bye.")
      #list high-score table
   elif choice =="1":
      print("High Scores")
      for item in Scores:
         print(item)
            #add a score
   elif choice =="2":
      score = int(input("what score did you get?:"))
      Scores.append(score)
      print(Scores)
      #remove a score
   elif choice =="3":
      score = int(input("Remove which score?:"))
      if score in Scores:
         Scores.remove(score)
         print(Scores)
      else:print(score,"isn’t in the high scores list.")
      #sort scores
   elif choice =="4" :
      Scores.sort(reverse= True)
      print(Scores)
      #some unkownchoice
   else:
      print("Sorry, but", choice, "isn’t a valid choice.")
input("\n\nPressthe enter key to exit")
