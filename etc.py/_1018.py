import sys 

input = sys.stdin.readline

n1,n2 = map(int,input().split())
count = [0,0]
board = [[0 for _ in range(n2)]for _ in range(n1)]
cnt = []
for i in range(n1) :
   color = input()
   for a,b in zip(color,range(n2)) :
         board[i][b] = a

for i in range(n1-7) :
  for t in range(n2-7) :
    w = 0
    b = 0
    
    
    for s in range(i,i+8) :
      for j in range(t,t+8) :
         
         
              
              if (s+j)%2 == 0 :
                 if board[s][j] == 'B' :
                      w += 1
                 else : 
                      b += 1
              else :
                 if board[s][j] == 'B' :
                     b += 1
                 else :
                      w += 1
    cnt.append(w)
    cnt.append(b)
              
print(cnt)
print(min(cnt))
