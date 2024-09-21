import sys
from collections import deque 

input = sys.stdin.readline

n = int(input())

n_array = [int(input()) for _ in range(n)]
msg = deque()
stack_array = deque()


n_append = 1


for num in n_array :
  
  
      
  
  while n_append<=num : 
    
    stack_array.append(n_append)
    msg.append("+")
    n_append += 1
    
    
  
  if(stack_array[-1]>num) :
    print("NO")
    sys.exit()
  
  else :
    stack_array.pop()
    msg.append('-')
    

    

    

for i in msg:
    print(i)  