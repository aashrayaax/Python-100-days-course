for i in range(5):
    print(i)
    if i == 4:
        break    
else : 
    print("No i")    



for i in range(5):
    print(f"Current iteration: {i}")
    if i == 2:
        print("Breaking the loop")
        break
    print("This will not be printed after the break")

print("This code is after the loop and will always execute.")  


for x in range(5):
    print ("iteration no {} in for loop".format(x+1))
else:
    print ("else block in loop")
print ("Out of loop")
