import random

word_list=["assddskfgj","sadadad","asdasdgb"]
life=6

pb = random.choice(word_list)
print(pb)

pa = '_'*len(pb)
print(pa)

gameover = False

ca = []


while not gameover :

  answer = input("Guess a letter :").lower()
  print(answer)
  c = False

  display=""

  for letter in pb :
   if(letter==answer) :
     display += letter
     ca.append(letter)
     c = True

  
   elif(letter in ca) :
     display+=letter
  
   else : 
     display += '_'
  
  
  if(not c):
    life -=1
    if(life==0) :
      gameover = True
      print("You Lose!")
      print("정답 :"+pb)
      break
  
  if(display==pb) :
    gameover = True
    print("You Win!")
    
  
  print(display)
  
  

    







