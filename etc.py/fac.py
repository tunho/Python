import sys 
def fac (n) :
    if n == 0 :
        return 1
   
    if n <2 :
        return n 
    
    
    
    return n*fac(n-1)
input = sys.stdin.readline

n,m = map(int,input().split())



print(fac(n)//(fac(m)*fac(n-m)))