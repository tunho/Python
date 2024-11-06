# import sys


# def cal(floor,num) :
#   if floor == 0 :
#     return num
#   else : 
#     return_n = 0
#     for i in range(num) :
#        return_n += cal(floor-1,num-i)
#     return return_n
# input = sys.stdin.readline

# n = int(input())

# for _ in range(n) :
#   floor = int(input())
#   num = int(input())
#   print(cal(floor,num))
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):  
    floor = int(input()) 
    num = int(input())  
    floor_0 = [x for x in range(1, num+1)]  
    for _ in range(floor):  
        for i in range(1, num):  
            floor_0[i] += floor_0[i-1]  
    print(floor_0[-1])  



  