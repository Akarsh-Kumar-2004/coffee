def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
user_num1 = float(input("Enter first number :"))
should_continue = True
while(should_continue == True):
    user_symbol = input("choose a symbol ( + - * / )")
    user_num2 = float(input("Enter second number :"))
    calc_dict = {"+":add,"-":sub,"*":mul,"/":div}
    answer = calc_dict[user_symbol]
    print(f"{user_num1} {user_symbol} {user_num2} = {answer(user_num1,user_num2)}")
    user_nextcalc = input("want to calculate further ? (Y/N)")
    if(user_nextcalc == "Y" or "y"):
        user_num1 = answer(user_num1,user_num2)
    else:
        should_continue = False
        print("********EXIT********")
     


    



