MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 30,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 25,
    }
}

resources = {
    "profit":0,
    "water": 300,
    "milk": 200,
    "coffee": 100,
}







def resource_availibilty(ingr):
    for i in ingr:
        if resources[i] >= ingr[i]:
            return True
    return False










def money_calc(beverage_cost):
    rup1 = int(input("Enter the number of 1 rupee coins: "))
    rup2 = int(input("Enter the number of 2 rupee coins: "))
    rup5 = int(input("Enter the number of 5 rupee coins: "))
    rup10 = int(input("Enter the number of 10 rupee coins: "))
    total = rup1+rup2*2+rup5*5+rup10*10
    if (total >=beverage_cost):
        money_to_be_returned =  total - beverage_cost
        resources["profit"] = resources["profit"] + beverage_cost
        print(f"Giving you {money_to_be_returned} rupees back")
        #print(resources["profit"])
    else:
        print("given money is insufficient :(")
        
        
        
        
        
def beverage_making(coffee_ingridients):
    for x in coffee_ingridients:
        resources[x] = resources[x] - coffee_ingridients[x]
    print("here is your coffee 🍵 !!!")
        #print(resources)
        
        
        
        
        
        
        
        
        
        
flag = 1
while flag !=0:
    
    user_input = input("what would you like ? (espresso/latte/cappuccino) :")
    if (user_input== "off"):
        print("turning off ")
        flag = 0
    elif (user_input== "report"):
        print(f"{resources['water']} ml .........{resources['milk']} ml.........{resources['coffee']} mg.........{resources['profit']} rupees")
    elif(user_input.lower() == "espresso"):
        drink = MENU["espresso"]
        print(drink)
        if resource_availibilty(MENU["espresso"]["ingredients"]):
            print(MENU["espresso"]["cost"])
            money_calc(MENU["espresso"]["cost"])
            beverage_making(MENU["espresso"]["ingredients"])
    elif(user_input.lower() == "latte"):
        drink = MENU["latte"]
        print(drink)
        if resource_availibilty(MENU["latte"]["ingredients"]):
            print(MENU["latte"]["cost"])
            money_calc(MENU["latte"]["cost"])
            beverage_making(MENU["latte"]["ingredients"])
    elif(user_input.lower() == "cappuccino"):
        drink = MENU["cappuccino"]
        print(drink)
        if resource_availibilty(MENU["cappuccino"]["ingredients"]):
            print(MENU["cappuccino"]["cost"])
            money_calc(MENU["cappuccino"]["cost"])
            beverage_making(MENU["cappuccino"]["ingredients"])
            
            
        else:
            print("SORRY..........insufficent amount of ingredients left :(")
        
        
        
    
    

