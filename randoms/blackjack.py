import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealer_card_1 = random.choice(cards)
dealer_card_2 = random.choice(cards)
user_card_1 = random.choice(cards)
user_card_2 = random.choice(cards)
dealer_check_21 = dealer_card_1+dealer_card_2
user_check_21 = user_card_1+user_card_2


if(dealer_check_21>21 and dealer_card_2 == 11):
    dealer_card_2 = 1
    dealer_check_21 = dealer_card_1 + dealer_card_2
if(user_check_21>21 and user_card_2 == 11):
    user_card_2 = 1
    user_check_21 = user_card_1+user_card_2

    



if (user_check_21>21):
    print("Dealer won :( ")
    exit
elif(dealer_check_21 == 21):
    print("Dealer won :( ")
    exit
elif(user_check_21 == 21):
    print("You won !!! ")
    exit
else:
    print("aage baaki hai")
    

    
