import sys
import random

def game() :
      print("Welcome to the Number Guessing Game!")
      print("I'm thinking of a number between 1 and 100 " )
      level = input("Choose a difficulty. Type 'easy or hard : ")
      chance = 0
      C_ANSWER = random.randint(1,100)
      if level =="hard" :
        chance = 5
      elif level == "easy" :
        chance = 10
      
        
        
      while chance >=0 :
          print(f"Yoy have {chance} attempts remaining to guess the number. ")
          y_answer = int(input("Make a guess : "))
          if y_answer > C_ANSWER :
            print("TOO high.")
            print("Guess again.")
            chance -= 1
          elif y_answer < C_ANSWER :
            print("TOO low.")
            print("Guess again.")
            chance -= 1
          else : 
            print(f"You got it! The answer was {C_ANSWER}")
          if chance == 0 :
            print("You've run out of guesses, you lose. ")  
            break

game()   




