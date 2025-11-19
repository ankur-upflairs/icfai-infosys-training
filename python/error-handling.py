# print("hello")
# x=10/0
z=45
# try:
#     y=z+'a'
# except Exception as e:
#     print('error occured',e)
# try:
#     x=10/0 
#     y=z+'a'
# except TypeError as e:
#     print('error occured',e)
# except ZeroDivisionError as e:
#     print(e) 
try:
    y=z+9
except Exception as e:
    print('error occured',e)
else:
    print('there is no error in code')
finally:
    print('try-except block complete')

def non_negetive(n):
    if n<0:
        raise ValueError("number can't be empty")
    return n
try:
    non_negetive(-5)
except ValueError as e:
    print(e)
# print(x,y)

