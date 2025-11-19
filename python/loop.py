# loop => to repeat a code 
#starting of a loop
# i =1 
# while i<11 :#end condition
#     print(i)
#     i+=1#updatation
# 10-1 
# i=10
# while i>0:
#     print(i)
#     i-=1
# for i in range(50,101,2):
#     print(i)

# 1 100 => skipping 3 no
# 100-1 => 5(skip) 
#take a no. and print its table 
#take a no from user and count its digits
#without len function
#sum of digits 
#print 1-100 but if a no is divisible by 3 =>'hey
#5=>'bye' otherwise print no.
# for i in range(1,101,4):
#     print(i)
# for i in range(100,0,-6):
#     print(i)
n=input('enter a no: ')
count= 0
# for i in str(n):
#     count+=1
# else:
#     print(count)
# n=int(n)
# while n>0:
#     n//=10
#     count+=1
# print(count)
#continue => go to next iteration 
#break =>exit the loop
#print 1-50if n is divisible by 5 than dont 
#print  and if n is divisible by 27 than exit
# for i in range(1,51):
#     if i%5==0: 
#         continue
#     if i%27==0: break
#     print(i)
#nest => loop inside loop
c=1
for i in range(4):
    for j in range(i+1):
        print(c,end=' ')
        c+=1
    print()
