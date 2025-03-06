import random
#sabse pehle humne user se input liya ....user 0,1,2 mein se kuch select karega
user_choice = int(input("Enter rock(0) , paper(1) or scissors(2) : "))
#ab computer ko choose karne bola.....random function lagaya aur 0,1,2 mein se koi ek randomly choose karwaya
ai_choice = random.randint(0,2)


#ab print karwaya ki user ne kya choose kiya hai
if(user_choice == 0):
    print("you chose 👊")
if(user_choice == 1):
    print("you chose ✋")
if(user_choice == 2):
    print("you chose ✌️")
    
    
    
#phir print karwaya ki computer(AI) ne kya choose kiya
if(ai_choice == 0):
    print("AI chose 👊")
if(ai_choice == 1):
    print("AI chose ✋")
if(ai_choice == 2):
    print("AI chose ✌️")


# ab main cheez.......if else statement - 
#maine kaise kiyamai batata hu......so hum log either saare win cases ko mention kar sakte hai and last mein else mein loss ka
# situation laga denge ya toh vice-versa
# maine saare user ke win waale cases mention kiye hai
# kaise kiya ??........
if(ai_choice == user_choice):
    #agar dono ne same choose kiya toh tie
    print("oops ...It's a TIE :) ")
elif(ai_choice == 0 and user_choice == 1):
    #agar ai rock choose kiya and user ne paper toh user jeeta
    print("YOU WIN !!! ")
elif(ai_choice == 1 and user_choice == 2):
    #agar ai ne paper choose kiya and user ne scissor toh user jeeta
    print("YOU WIN !!! ")
elif(ai_choice == 2 and user_choice == 0):
    print("YOU WIN !!! ")
elif(user_choice>2):
    # agar user ne kuch galat input kiya....ya 0,1,2 mein se kuch enter nahi kiya toh phir user haar gaya aisa command diya maine
    print("Invalid input......YOU LOSE :( ")
    # ab user sirf 3 cases mein jeet sakta hai and baaki kisi mein nahi......and 3 cases maine uparmention kar diya hai so jo else
    # statement hai usmein you lose waala command diya
else:
    print("YOU LOSE :( ")
