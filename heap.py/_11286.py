# 최소 출력 힙
import heapq
import sys 

input = sys.stdin.readline

n = int(input())

h_list = []
for _ in range(n) :
  num = int(input())
  if num == 0 :
    if h_list :
      print(heapq.heappop(h_list)[1])
    else : 
      print(0)
  else :
    heapq.heappush(h_list,(abs(num),num))
