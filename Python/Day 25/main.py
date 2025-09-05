tuple1 = (1,8,2,7,63,1,7,2,72,7,2,752,752,78,1,58632)
temp = list(tuple1)
temp[0] = 555555555
tuple1 = tuple(temp)
print(tuple1)

countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)

Tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = Tuple1.count(3)
print('Count of 3 in Tuple1 is:', res)


Tuple = (0, 1, 2,  2, 3, 1, 3, 2)
res = Tuple.index(3)
print('First occurrence of 3 is', res)