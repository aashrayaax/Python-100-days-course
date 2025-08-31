a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
if(a+b == 10):
    print("The sum is 10")

    # these are few applications

# atm

a = int(input("Enter the amount : "))
if(a>10000):
    print("Sorry,This Atm machine currently has 10000 cash only.Can you enter a lesser amount?")

# shopping cart

a = int(input("Whats the total bill of this customer?"))
if(a>999):
    print("Free shipping is applicable for this order")



# ac at home
temp = int(input("Whats the current temperature of the room?"))
if(temp <= 20):
    print("Automatically turn off the ac")

# steps counter

steps = int(input("Enter the number of steps taken by the user today"))
if(steps>=10000):
    print("Hurray!!You finished your 10k step count for todayyyyyyyyyyyyyyyyyyyyyyyyyyy")