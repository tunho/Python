# 21 초과시 에이스 11 - > 1 인 것 확인(x)
import random 
from s_79 import deal_card
def calculate_score(cards) :
  if sum(cards) == 21 and len(cards) == 2: #11 in cards and 10 in cards and len(cards) == 2: # black jack 확인
    return 0
  if 11 in cards and sum(cards) :
    cards.remove(11)
    cards.append(1)
  
  return sum(cards) # 파이썬 내장함수 리스트 이용가능
def compare(u_score , computer_score) : # 우클릭하면 똑같은 이름 동시에 이름변경 가능한 기능존재
  if u_score == computer_score :
    return "draw"
  elif u_score > 21 :
    return "You went over. You lose"
  elif computer_score > 21 :
    return "Opponent went over. You win."
  elif u_score > computer_score :
    return "You win"
  else : 
    return "You lose"
def play_game() :
    user_cards = [] 
    computer_cards = []
    computer_score = -1 # 36번째줄 해결 
    is_game_over = False
    for _ in range(2) :
      user_cards.append(deal_card())
      computer_cards.append(deal_card())

    while not is_game_over :
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"computer cards: {computer_cards[0]}")

        if user_score > 21 :
          is_game_over = True
        else : 
          user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
          if user_should_deal == 'y' :
            user_cards.append(deal_card())
          else : 
            is_game_over = True
    while computer_score < 17 : # 위 while문이 실행되지 않으면 computer_score는 없음. 
      computer_cards.append(deal_card())
      computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score,computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y" :
  play_game()