class myclass:
    x=5
    print(x)

myclass

#object 
class myclass1:
    a=10

obj=myclass1()
print(obj.a)


#__init__

class abc:
    def __init__(self,name,age):
        self.name=name
        self.age=age

p1=abc("xyz",20)
print(p1.name)
print(p1.age)


#getdata function
class abcd:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def getData(self):
        print("Name is :",self.name)
        print("Age is :",self.age)

p2=abcd("mnbg",20)
p2.getData()

#getdata function
class abcd1:
    def __init__(ab,name,age):
        ab.name=name
        ab.age=age
    
    def getData(as1):
        print("Name is :",as1.name)
        print("Age is :",as1.age)

p21=abcd1("mnbg",20)
p21.getData()