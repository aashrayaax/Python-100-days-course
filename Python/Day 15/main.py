import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)

H = int(time.strftime('%H'))
print(H)

M = int(time.strftime('%M'))
print(M)

S = int(time.strftime('%S'))
print(S)
if(H>=4 and H<12):
    print("Good Morning")
elif(H>=12 and H<16):
    print("Good Afternoon")
elif(H>=16 and H<20):
    print("Good Evening")
else:

    print("Good Night")    


# https://docs.python.org/3/library/time.html#time.strftime