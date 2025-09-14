marks = [52,9,56,46,9,6,59,89,98,53,65,45,75]
for mark in marks:
    print(mark)
    
    if(mark == 4):
        print("Good jobbbbbbbbbbbb")


marks = [52,9,56,46,9,6,59,89,98,53,65,45,75]
for mark in marks:
    print(mark)    
    if(mark == 4):
        print("Good jobbbbbbbbbbbb")



index = 0 
list = ["milk","bread","eggs"]
for item in list:
     
    if(index==0):
        print("grab milk ")   
    if(index==1):
        print("grab bread")        
    if(index==2):
        print("grab eggos ")
    index = index +1         


list = ["milk","bread","eggs"]

for index, item in enumerate(list):
    print(f"Index: {index}, Item: {item}")    