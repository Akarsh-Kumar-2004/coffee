a = int(input("Enter the year :"))
if(a<=0):
    print("*************************invalid input !!!**************************")
elif(a%4==0):
    if(a%100==0):
        if(a%400==0):
            print("A leap year !!! ")
        else:
            print("not a leap year :( )")
            exit
    else:
        print("A leap year !!!")