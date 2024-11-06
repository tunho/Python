# 계산기
# 함수() <- 함수를 실행 시킴
def add(n1,n2) :
  return n1+n2
# my_favourite_operation = add # add 함수가 새로운 참조가 만들어짐

# print(my_favourite_operation(1,3))

# TODO: Write out the other 3 functions - subtract, multiply and divide.

def subtract(n1,n2) :
  return n1-n2
def multiply(n1,n2) :
  return n1*n2 
def divide(n1,n2) :
  return n1/n2

# TODO : Add these 4 functions into dictionary as the values. Keys = "+" , "-" , "*" , "/"

operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide
}

# operations["+"] = add
# operations["-"] = subtract
# operations["*"] = multiply
# operations["/"] = divide

# TODO : Use the dictionary operations to perform the calculations. 
print(operations["*"](4,8))

# TODO : Make main to use functions and dictionary and complete project

def calculation() :
  boool = True 
  n1 = float(input("값을 입력 : "))
  while boool : 
    
    for i in operations : 
      print(i,end=" ")
    operation = input("\n연산자 입력 : ")
    excute = operations[operation]
    n2 = float(input("값을 입력 : "))
    #print(excute(n1,n2)) 
    answer = operations[operation](n1,n2)
    print(f"{answer}")
    print(f"continue with{answer}? or do with a new calculation ")
    choice = input("")

    if choice == "y" : 
        n1 = answer
    else : 
        boool = False
        print ("\n" * 20)
        calculation()


calculation()   







