dict = {
    "a" : "gfcvjshg",
    "b" : "fchgjhgjh"
}
print(dict)
print(type(dict))

dic = {
    "Harry" : "Human",
    "Monitor" : "Object"
}
print(dic["Harry"])

info = {'name':'Karan', 
        'age':19,
          'eligible':True}
print(info)
print(info.keys())
print(info.values())
print(info["eligible"])

for key in info.keys():
    print(f"The values are {info[key]}")


info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.items())    