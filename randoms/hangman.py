import random
print("**********************THE HANGMAN GAME************************")
list_of_words = ["Mystery","Pineapple","Extravagant","Accordion","Galvanize","Benevolent","Kaleidoscope","Umbrella","Zephyr","Eclipse"]
word = random.choice(list_of_words).lower()
print(word)
#user_input = input("Guess a letter : ").lower()
# for i in word:
#     if i == user_input:
#         print("Right")
#     else:
#         print("wrong")
# list_of_spaces = []
# for i in word:
#     list_of_spaces.append("_")
# print(list_of_spaces)
flag = 0
list_of_spaces = []
while flag !=1:
    user_input = input("Guess a letter : ").lower()
    for i in word:
        if i == user_input:
            list_of_spaces.append(i)
        else:
            list_of_spaces.append("_")
    print(list_of_spaces)
if "_" not in list_of_spaces:
    print("YOU WIN")
    flag = 1