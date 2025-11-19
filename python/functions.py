# def sum(a,b):
#     return a+b 
# print(sum(4,6))
# def sum(*args):
#     print(args)
# sum(4,5,6,7,8,9)
#function => list =>
#select 1.insert =>index, element
# 2.update  =>index, value
# 3.delete  =>index 
# 4.show  => 
# again or exit
# def choice(l):
#     c= int(input('''1. for exit 
#              2. for continue
#                  '''))
#     if c==2:
#         operations(l)


# def operations(l):
#     op=int(input('''Enter operation :-
#            1. for insert
#            2.for update'''))
#     if op==1 :
#         i=int(input('enter index : '))
#         e=input('Enter value: ')
#         l.insert(i,e)
#         print(l)
#         choice(l) 

# operations([1,2,3,4])
# def show(**kwargs):
#     for i,j in kwargs.items():
#         print(i,j)
# show(name='pawan',age=34,profession='teaching')

# def count(n):
#     if n==0:
#         return
#     count(n-1)
#     print(n)
# count(10)
# def sum(n):
#     if n==1:
#         return 1
#     return n + sum(n-1)
# print(sum(10))
#global
a=45
def x():
    b=12 #local variable
    global a
    a+=5
    print(a)
    def y():
        nonlocal b 
        b+=3
        print(b)

        c=34
    y()
# print(b)
x()




