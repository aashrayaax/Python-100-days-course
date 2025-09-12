a = input("Enter a number : ")
print(f"The multiplication table of {a} is")
try:
   for i in range(1,13):
       print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:
    print(e)
print("This is the most important part of the program")   


try:
    num = int(input("Enter an integer: "))
    print("Ok , Its good that you entered an integer")
except ValueError:
    print("Number entered is not an integer.")


try:
    a = int(input("Enter a number : "))
    b = int(input("Enter another number  : "))
    solution = (a)/(b)
    print(solution)
except ZeroDivisionError:
    print("How can we divide with zero bruh,enter an integer") 
except ValueError:
    print("Bruh, Enter a number.How can we perform division for strings")
else:

    print("No exceptions were raised")         


try : 
    a = int(input("Enter a number"))
    print(a)
except Exception as e:
    print(e)
print("Blah B;ah Blah")        
