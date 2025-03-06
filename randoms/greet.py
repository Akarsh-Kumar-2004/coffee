import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
time_hour = int(time.strftime('%H'))
print(time_hour)
# timestamp = time.strftime('%H')
# print(timestamp)
# timestamp = time.strftime('%M')
# print(timestamp)
# timestamp = time.strftime('%S')
# print(timestamp)
# https://docs.python.org/3/library/time.html#time.strftime
if (5<=time_hour<12):
    print("Good Morning !!!")
elif(12<=time_hour<18):
    print("GOOD AFTERNOON")
elif(18<=time_hour<20):
    print("GOOD EVENING")
else:
    
    print("GOOD NIGHT   zzzz") 
print(4%2)
