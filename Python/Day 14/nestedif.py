
# num = 18
# if (num < 0):
#     print("Number is negative.")
# elif (num > 0):
#     if (num <= 10):
#         print("Number is between 1-10")
#     elif (num > 10 and num <= 20):
#         print("Number is between 11-20")
#     else:
#         print("Number is greater than 20")
# else:
#     print("Number is zero")






# loan eligibility
# age = int(input("Enter age : "))
# if (age >= 18):
#     income = int(input("Enter your montly salary : "))
#     if (income >= 30000): 
#         print("Eligible for loan");
#     else :
#         print("Income too low");
# else :
#     print("Underage")


# grading system 

# score = 92

# if score >= 80:
#     if score > 90:
#         print("Grade: A+")
#     else:
#         print("Grade: A")
# else:
#     print("Grade: Below A")



# vehicle saftey check
engine_on = True
seatbelt_fastened = True

if engine_on:
    if seatbelt_fastened:
        print("🚙 Ready to drive")
    else:
        print("🔔 Please fasten seatbelt")
else:
    print("🔧 Start the engine first")