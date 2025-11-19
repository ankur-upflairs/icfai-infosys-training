a=[34,23,12,9]
# print(len(a))
# print(a.append(33),a)
# a.extend([3,4])
# a.insert(1,56)
# a.pop(1)
# a.clear()
# a.remove(34)
# a.reverse()
# a.sort(reverse=True)
# b='hello'
# c=list(b)
# f=['a','b']
# e='-'.join(f)
# print(e)
# for i in a:
#     print(i)

a=[34,23,12,9]
#index => element=> insert but using loop
i=int(input('enter index : '))
if i not in range(len(a)):
    print('wrong index')
else:
    e=input('enter element : ')
    f=[]
    # for j in range(i):
    #     f.append(a[j])
    # f.append(e)
    # for k in range(i,len(a)):
    #     f.append(a[k])
    for j,k in enumerate(a):
        if i==j:
            f.extend([e,k])            
        else:
            f.append(k)
    print(f)

#delete an element at specific index using loop
