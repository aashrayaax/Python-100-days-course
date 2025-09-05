l = [1,5,1,4,8,2,4,5,10,9,8,6,54,2,78,45,55]
m = [" jhcbgskjdc",4565,465,8779]
l.append(45)
l.sort()
l.sort(reverse=True)
p = l.index(45)
p = l.count(2)
print(p)


a = l
a[1] = 5555555
print(l)

l.insert(4,44444444444)
print(l)

l.extend(m)
print(l)

print(l + m)

