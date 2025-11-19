# class University:
#     name="icfai"
# mnit=University()
# University.name='rtu'
# print(mnit.name)
# abc=University()
# print(abc.name)
# class Animal:
#     def __init__(self,name,eye_color):
#         self.name=name#instance variable
#         self.eye_color=eye_color
#     def show(self):
#         print(f"name={self.name} and color = {self.eye_color}")


# dog=Animal('softy','black')
# print(dog.name,dog.eye_color)
# dog.show()
# cat = Animal('tom','blue')
# print(cat.name,cat.eye_color)
# cat.show()  
# single inheritance 
# class Parent:
#     def parent_details(self):
#         print('parent called')
# class Child(Parent):
#     def child_details(self):
#         print('child called')

# a=Child()
# a.child_details()
# a.parent_details()
# class GrandParent:
#     def grand_details(self):
#         print('grand parent class called')
# class Parent(GrandParent):
#     def parent_details(self):
#         print('parent called')
# class Child(Parent):
#     def child_details(self):
#         print('child called')

# a=Child()
# a.child_details()
# a.parent_details()
# a.grand_details()
# class Father:
#     def father_details(self):
#         print('father class called')
# class Mother:
#     def mother_details(self):
#         print('mother called')
# class Child(Father,Mother):
#     def child_details(self):
#         print('child called')

# a=Child()
# a.child_details()
# a.father_details()
# a.mother_details()

# class Parent():
#     def parent_details(self):
#         print('parent called')
# class Child1(Parent):
#     def child1_details(self):
#         print('child1 called')
# class Child2(Parent):
#     def child2_details(self):
#         print('child2 called')
# a=Child1()
# a.parent_details()
# b=Child2()
# b.parent_details()
class A:
    def __init__(self,a):
        self.a=a
    def show(self):
        print('class a')
class C:    
    def show(self):
        print('class c')

class B(A,C):
    def __init__(self,a,b):
        super().__init__(a)
        self.b=b        
    def show(self):
        print('class b') 


c= B(4,5)
c.show()
print(B.mro())

