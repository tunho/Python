# 최소 공배수 최대 공약수
import sys
input = sys.stdin.readline

n,m = map(int , input().split())

smallest = min(n,m)
result1 = 1
result2 = n*m 
for i in range(1,smallest+1) :
  if(n%i==0 and m%i == 0) :
    result1 = i
  
result2 = result2 // result1

print(result1 , result2)