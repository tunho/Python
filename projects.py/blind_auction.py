import sys 

#input = sys.stdin.readline

bids = {}
continue_bidding = True

while continue_bidding :
 print("Welcome to the secret auction program")
 name = input("What is your name? : ")
 price = int(input("What is your bid? : $"))
 bids[name] = price
 print("Is there other user who want to bid?")
 answer = input()
 if(answer == "No") :
  continue_bidding = False
 else : 
  print('\n'*20)

highest = 0
winner = ""

''' max(bids, key=bids.get) 
== ''' # <- docstrings 
for name in bids :
 bid_ammount = bids[name]
 if (bid_ammount > highest) :
  highest = bids[name]
  winner = name
print(f"The winner is {winner} with a bid ${highest}")
  

   




