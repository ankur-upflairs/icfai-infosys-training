# file = open('sample.txt','r+')
# # print(file.name)
# print(file.read())
# # print(file.readlines())
# file.write('new text added')
# print(file.read())
# file.close()
# file = open('sample.txt','a+')
# print(file.read())
# # file.write('new text added')
# print(file.read())
# file.close()
# make a program to create 2-10 table in seperate
# files (eg. table of 2.txt )
# for i in range(2,11):
#     file= open(f"table of {i}.txt",'w')
#     for j in range(1,11):
#         file.write(f"{i} * {j} = {i*j} \n")
#     file.close()
# with open('sample.txt','r') as f:
#     # data = f.read()
#     # print(data)
#     for line in f:
#         print(line)
# import json
# with open('data.json','r') as f:
#     jsonData= f.read()
#     print(jsonData)
#     dict= json.loads(jsonData)
#     print(dict["name"])
import json
c=int(input('''1.for register
            2.login
            :'''))
def register():
    n=input('enter name: ')
    p=input('enter password : ')
    data = None
    with open('data.json','r') as f:
        x= f.read()
        data = json.loads(x)
        data.append({"name":n,"password":p})
    with open('data.json','w') as f:
        a=json.dumps(data)
        f.write(a)
def login():
    with open('data.json','r') as f:
        x= f.read()
        data = json.loads(x)
        if len(data) < 1:
            print('there is no user \n register first')
            return
        else :
            n=input('enter name: ')
            p=input('enter password : ')
            
if c==1:
    register()
elif c==2:
    pass
# with open('data.json','r') as f:
#     jsonData= f.read()
#     print(jsonData)
#     dict= json.loads(jsonData)
#     print(dict["name"])
