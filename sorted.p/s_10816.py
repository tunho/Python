from sys import stdin
import bisect
  
input = stdin.readline

card_n = int(input())

card_list = list(map(int, input().split()))

list_size = len(card_list)
card_list.sort()

predict_n = int(input())

predict_list = list(map(int, input().split()))


for i in predict_list :
  left_index = bisect.bisect_left(card_list,i)
  right_index = bisect.bisect_right(card_list,i)
  print(right_index-left_index,end=" ")

  