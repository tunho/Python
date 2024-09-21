from collections import deque
import sys

n=int(input(""))

d=deque()

while n>0 :
  msg = sys.stdin.readline().strip().split()

  if (msg[0]=="push") :
    d.append(int(msg[1]))
  
  elif (msg[0]=="pop") :
    if len(d)>0 :
      print(d.popleft())
    else :
      print(-1)
  
  elif (msg[0]=="size") :
      print(len(d))
  
  elif (msg[0]=="empty") :
    if(len(d)==0) :
      print(1)
    else : 
      print(0)
  
  elif (msg[0]=="front") :
    if(len(d)>0) :
      print(d[0])
    else :
      print(-1)
  
  elif (msg[0]=="back") :
    if(len(d)>0) :
      print(d[-1])
    else :
      print(-1)
  n-=1
