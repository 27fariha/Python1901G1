class myclass:
    x=5
    print(x)
    z=10

myclass

#object 
class myclass1:
    a=10

obj=myclass1()
print(obj.a)


#__init__
#work constructor
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

#getdata function with replace self keyword
class abcd1:
    def __init__(ab,name,age):
        ab.name=name
        ab.age=age
    
    def getData(as1):
        print("Name is :",as1.name)
        print("Age is :",as1.age)

p21=abcd1("mnbg",20)
p21.getData()

#update value 
class abc1:
    def __init__(self,name,age):
        self.fullname=name
        self.Age=age

p5=abc1("xyz",20)
p5.Age=50
print(p5.fullname)
print(p5.Age)

#Delete value 
class abc2:
    def __init__(self,name,age):
        self.fullname=name
        self.Age=age

p5=abc2("xyz",20)
del p5.Age
#del p5
print(p5.fullname)
#print(p5.Age)

#pass keyword
class myclass5:
  '''This is one text'''
  pass
print(myclass5.__doc__)


# instance , class and static me
class example:
    def method(self):
        return "Instance method called ",self
    @classmethod
    def classmethod(cls):
        return "Class Method called",cls
    @staticmethod
    def staticmethod():
        return "Static method called"

obj =example()
print(obj.method())

print(obj.classmethod())

print(obj.staticmethod())