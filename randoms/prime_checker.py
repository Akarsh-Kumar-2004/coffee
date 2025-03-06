def prime_checker(number):
    flag = 1
    for i in range(2,n):
        if (n%i==0):
            flag = 0
 
    if(flag == 0):
        print("Not a prime number :( ")
    else:
            
        print("A prime number !!! ")

n = int(input())
prime_checker(number = n)