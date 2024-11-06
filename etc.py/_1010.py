

def DFS (n,m,k=1) :
  global num
  if n == 0 :
    num += 1
    return 
  for i in range (k,m+1) :
     if visited[i] == False :
        visited[i] = True 
     DFS(n-1,m,i+1)
     visited[i] = False 

     
    



import sys 
input = sys.stdin.readline
num = 0
input_n = int(input())
for _ in range(input_n) :
    num = 0
    n,m = map(int,input().split())
    visited = [False] * (m+1)
    DFS(n,m,1)
    print(num)
