# a=[1,2,3,4]
# it=iter(a)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
class Count:
    def __init__(self,start):
        self.start=start
    def __iter__(self):
        return self
    def __next__(self):
        if self.start <=0:
            raise StopIteration
        self.start-=1
        return self.start
# for i in Count(6):
#     print(i)
# x=iter(Count(4))
# print(next(x))
# def x():
#     yield 1
#     yield 2
#     yield 3
# y=x()
# # print(next(y))
# for i in y:
#     print(i)
# def count(n):
#     a=0
#     while a <n:
#         yield a
#         a+=1
# for i in count(8):
#     print(i)
def show(fn):
    def add_info():
        print('start')
        fn()
        print('end')
    return add_info
# def greet():
#     print('hello everyone')

# greet= show(greet)
# greet()
@show
def greet():
    print('hello everyone')
greet()
