n1 = int(input(""))
n1_list = list(map(int , input().strip().split()))
n2 = int(input(""))
n2_list = list(map(int , input().strip().split()))
N=len(n1_list)
n1_list.sort()



for i  in n2_list :
  begin , end = 0 , N-1
  isCheck = False


  while begin <= end :
    mid = (begin+end)//2

    if(i>n1_list[mid]) :
      begin = mid+1
    elif(i<n1_list[mid]) :
      end = mid -1 
    else :
      isCheck = True
      break
    
  
  if(isCheck) :
    print(1)
  else : 
    print(0)


    
    

     








