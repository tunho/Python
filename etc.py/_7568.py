import sys

input = sys.stdin.readline

n = int(input()) # 사람 수 입력

p_size =[]
p_rank = []
for _ in range(n) : # n번 작성
  a,b = map(int , input().split())
  p_size.append([a,b])


for i in p_size : # 사람 리스트 출력
  rank = 1 # 순위 1등으로 초기화

  for compare in p_size : # 비교 대상 
    if i[0] < compare[0] and i[1] < compare[1] : # 둘 다 크면 랭크 +1
      rank += 1
  p_rank.append(rank)

print(*(p_rank))
  


