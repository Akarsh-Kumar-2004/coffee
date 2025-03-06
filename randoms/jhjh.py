import random
def deal_card():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10,10]
    return random.choice(cards)
user_cards=[]
computer_cards=[]
for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
print(user_cards)
print(computer_cards)

def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
        return 0
  if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
  return sum(cards)




game_end=False
while not game_end:
    user_score=calculate_score(user_cards)
    computer_score=calculate_score(computer_cards)
    print(f"Your cards:{user_cards}        your score:{user_score}")
    print(f"computer cards:{computer_cards[0]}")
    
    if user_score==0 or computer_score==0 or user_score>21:
        game_end=True
    else:
        continue_game= input("Would you like to draw another card?Type'y' or 'n'").lower()
        if continue_game=="y":
            user_cards.append(deal_card())
        elif continue_game=="n":
            game_end=True
            