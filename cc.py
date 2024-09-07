n=int(input(""))
n1_list = list(map(int , input().strip().split()))
result=sorted((set(n1_list)))


dic={result[i]: i for i in range(len(result))}


for i in n1_list :
  print(dic[i] , end= ' ')

