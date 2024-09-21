import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

list = []

for i in range(1,n//2+1) :
  list.append(i*2)


d = deque(list)
if(n==1) :
 print(1)
 sys.exit()
if(n==2) :
 print(2)
 sys.exit()
if(n==3) :
 print(3) 
 sys.exit()

n-=3
# 홀일때
if(n%2==0) :
 

 while 1 :
  if(n%2==0):
   d.rotate(-1)
   n-=1
  

  
  else :
   d.popleft()
   n-=1
   if(n==0) :
    print(d[0])
    sys.exit()
 # 짝일때
else :
 

 while 1 :
    if(n%2==1) :
     
      n-=1
      d.popleft()
     
      if(n<1) :
        print(d[0])
        sys.exit()
    else :
     d.rotate(-1)
     n-=1
  
