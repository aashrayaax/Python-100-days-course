for i in range (12):
    print("5 X " , i , "=",  5*i)

for j in range(15):
    if(j == 10):
        break
    print("5 X " ,j+1,"=", 5*(j+1))
   
for j in range(15):
    print("5 X " ,j+1,"=", 5*(j+1))   
    if(j == 10):
        break


print("Separator")  

i=1
while(i<=100):
    if(i==10):
        break
    print("5 X " , i , "=",  5*i)
    i = i + 1


for i in range(1,101):
    print(i ,end=" ")
    if(i==50):
        break
    else:
        print("Mississippi")
print("Thank you")


for i in range(10):
    print(i)
    if(i==5):
        continue
       
for i in range(3):
    print("Start of loop:", i+1)
    if i == 1:
        continue
    print("End of loop:", i+1)

for i in range(15):
    if(i==11):
        continue

    print("5 X " , i , "=",  5*i)
    


i = 100
while True:
    print(i)
    if i <= 10:
        break
    i -= 10  # Just an example to eventually meet the condition
print("breaked")



