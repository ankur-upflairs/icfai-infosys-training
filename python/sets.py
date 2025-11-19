# a={3,5,6}
# b=[3,4,6,7,3,6]

# print(set(b))
# for i in a:
#     print(i)
#mutable => element immutable
# c={45,'a',(4,5)}
# print(c)
# a.add(23)
# print(a)
# a.pop()
# a.remove(5)
# a.update([4,5])
# print(a)
# a={1,2,3,4}
# b={2,4,7,9}
# print(a.union(b))
# print(a.intersection(b))
# print(a-b)
# print(a.symmetric_difference(b))
a=[1,2,3,4,[5,6]]
# b=a
# b=a.copy()
# b[4][0]=11
# print(a,b)
# import copy
# c=copy.deepcopy(a)
# c[4][0]=11
# print(a,c)
b=a.copy()
a[0]=34
b[1]=55
print(a,b)
