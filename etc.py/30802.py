import sys

input = sys.stdin.readline

n = int(input())
T_shirts = list(map(int, input().split()))
T,P = map(int, input().split())
T_num = 0
for i in T_shirts :
  if(i%T==0) :
    T_num += i//T
  else :
    T_num += i//T + 1
print(T_num)
print(n//P,n%P)

  
    
