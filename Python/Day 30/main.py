
def fact(n):
    factorial = 1
    if(n == 0):
        print("Factorial is 1")
    else:
        for i in range(n,0,-1):
            factorial = factorial*i
    return factorial
print(fact(5) )       
        



 