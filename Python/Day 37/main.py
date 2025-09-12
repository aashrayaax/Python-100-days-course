def fun():
    try :
        l = [1,8,2.7,12,7,8,2,7,8,]
        a = int(input("Enter a number : "))
        print(l[a])
        return 1
    except:
        print("Some Error has occured")
        return 0
    finally:
        print("It will execute no matter what")    

sol = fun()
print(sol)


def fun():
    try :
        l = [1,8,2.7,12,7,8,2,7,8,]
        a = int(input("Enter a number : "))
        print(l[a])
        return 1
    except:
        print("Some Error has occured")
        return 0
    print("It will execute no matter what")    
sol = fun()
print(sol)   

