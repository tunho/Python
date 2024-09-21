import sys 
from collections import deque

input = sys.stdin.readline

str=""


while 1
 if(str==".\n"):
   break
 dq = deque()
 check = True

 for i in str :
  if(i=='(') :
    dq.append('(')
  elif(i==')') :
    if(len(dq)==0) :
      print('no')
      check = False
      break


    
    elif(dq.pop() == '(') : pass
      
    else : 
      print('no')
      check = False
      break
  
  
  elif(i=='[') :
    dq.append('[')
  
  elif(i==']') :
   
    if(len(dq)==0) :
      print("no")
      check = False
      break
    
    elif(dq.pop() != '[') :
      print("no")
      check = False
      break 
   
    else : pass
  else : pass 
 
 if  len(dq)==0 and check :
   print("yes")
 if len(dq)!=0 and check : 
   print("no")




 
  
     



