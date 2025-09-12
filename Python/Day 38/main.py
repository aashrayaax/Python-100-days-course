# salary = int(input("Enter salary amount: "))
# if not 2000 < salary < 5000:
#     raise ValueError("Not a valid salary")

# salary = int(input("Enter salary amount: "))
# if not 2000 < salary < 5000:
#     raise SalaryNotInRange("Not a valid salary")

a=input("Enter Please : ")
if (a=='quit') or (a== 'Quit'):
	print("Yes")
elif a.isnumeric():
	raise ValueError("Sorry enter quit")