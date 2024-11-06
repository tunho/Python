# blackjack
import random
is_21 = False
def deal_card() : 
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] # 덱은 무한이라고 가정
  card = random.choice(cards)
  return card
def over_21 (total) : 
  return total > 21 
def equal_21 (total) :
  return total == 21
def hit() : 
  card = deal_card()

  

def over_16(d_total) :
  return d_total > 16 
def choice (p_list,p_total,d_list,d_total) :
  if p_total == 21 :
    print("Black Jack")
    dealer_turn(p_list,p_total,d_total,d_list)
    return
  global is_21 
  while p_total <= 21 :
    
    print("hit or stand?")
    answer = input("")
    if (answer == "hit") :
      card = deal_card()
      p_list.append(card)
      p_total += card
      if p_total == 21 :
        print(p_total)
        print(f"{p_list}")
        is_21 = True
        dealer_turn(p_list,p_total,d_total,d_list)
        return
      if p_total > 21 and 11 in p_list :
        p_total -= 10 
        p_list.remove(11)
        p_list.append(1)
      print(f"player total = {p_total}")
      print(f"player cards = {p_list}")
    else : 
      dealer_turn(p_list,p_total,d_total,d_list)
      return
    
  

  print(f"dealer total = {d_total}")
  print(f"dealer card = {d_list}")  
  print("you lose")
def dealer_turn(p_list,p_total,d_total,d_list) :
  global is_21
  print(f"dealer total = {d_total}") 
  print(f"dealer card = {d_list}")  
  if d_total == 21 :
    if is_21:
      print("Draw")
    else : 
      print("you lose")
    return
  while (d_total <= 21) :
    if d_total < 17 :
      card = deal_card()
      d_list.append(card)
      d_total += card
      if d_total == 21 :
        if is_21 :
          print("Draw")
        else : 
          print("you lose")
          return
      if d_total > 21 and 11 in d_list :
          d_total -= 10 
          d_list.remove(11)
          d_list.append(1)
      print(f"dealer total = {d_total}")
      print(f"dealer cards = {d_list}")
      continue
    else : 
      if(d_total>p_total) :
        print("you lose")
        return
      elif(d_total < p_total) :
        print("you win") 
        return
      else : 
        print("draw")
        return
      
  print("you win")

if __name__ == "__main__" :
    p_card1 = deal_card()
    p_card2 = deal_card()
    p_list = [p_card1,p_card2]
    p_total = p_card1 + p_card2
    print(f"player total = {p_total}")
    print(f"player cards = {p_list}")
    d_card1 = deal_card()
    d_card2 = deal_card()
    d_list = [d_card1,d_card2]
    d_total = d_card1 + d_card2
    print(f"dealer tortal = x+{d_card2}")
    print(f"dealer cparcelaard = x,{d_card2}")
    choice(p_list,p_total,d_list,d_total)

  












