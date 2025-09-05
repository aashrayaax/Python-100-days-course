# def average(a,b):
#     av = (a+b)/2
#     print("The avg is", av)
# average(10,20)

def average(a=2,b=4):
    av = (a+b)/2
    print("The avg is", av)
average()
average(10,20)
average(a=123)
average(b=14)

def name(first,middle,last="David"):
    print("My Full name is" , first, middle ,last)
name("Amy","Ferrah","Fowler")  

# default arguments
def name(fname, mname = "Jhon", lname = "Whatson"):
    print("Hello,", fname, mname, lname)

name("Amy")

# keyword arguments: while calling function key and its value is given
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name(mname = "Peter", lname = "Wesker", fname = "Jade")

# Required arguments: mandatory ones,the number of arguments initialized should be satisfied
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)
name("ashu" ,"basva","murthy")
# name("Peter", "Quill")  this is error

# variable length arguments:can be initialized as dict or tuple
def name(*name):
    print("Hello,", name[0], name[1], name[2])

name("James", "Buchanan", "Barnes")


def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname = "Buchanan", lname = "Barnes", fname = "James")


def double_with_print(x):
    print(x * 2)

def double_with_return(x):
    return x * 2

# Using print
result1 = double_with_print(5)
print("Result1:", result1)  # Output: 10 (from inside function), then None

# Using return
result2 = double_with_return(5)
print("Result2:", result2)  # Output: 10