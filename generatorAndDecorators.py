# iterator => loop
#stopIteration
#next(), iter()

test_list=[1,2,3,4,5]
ab=iter(test_list)
#1st method
print(next(ab))   #1
#2nd method
print(ab.__next__())  #2
print(ab.__next__())    #3
print(ab.__next__())    #4
print(ab.__next__())    #5
#print(ab.__next__())    #error 

#perform by for 
for i in  test_list:
    print(i)

print("Custom Iterators")
#custom iterators
class PowerofTwo:
    def __init__(self, max = 0):
        self.maximum=max

    def __iter__(self):
        self.num=0
        return self
    def __next__(self):
        if self.num <= self.maximum :
            output=2**self.num
            self.num +=1
            return output
        else:
            raise StopIteration

power=PowerofTwo(4)
a=iter(power)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))


#perform by for 
for j in PowerofTwo(4):
    print(j)

#generators 

# basic fun disnot support multiple return statement
def showmsg():
    return "Hello world"
    #return "Python Programming"

print(showmsg())


#gen
def test_gen():
    num =1
    print("First Print") # 1
    yield num # return   # 2

    num +=1
    print("Second Print")
    yield num #2

    num +=1
    print("Third Print")
    yield num #3

#print
gen_obj=test_gen()
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))

#using generator with loop
def str_revers(word):
    length =len(word)
    for k in range(length -1,-1,-1):
        yield word[k]

#printing 
for i in str_revers("python"):
    print(i)



# Decorators : different method for calling a function 
def printetr(msg):
    print(msg)

#1st method
printetr("Hello world")

#2nd method
printer1=printetr
printer1("Hello world")

def incre(num):
    return num+1
def dec(num):
    return num -1
def ope(function,num):
    result=function(num)
    return result

print(ope(incre,5))
print(ope(dec,8))

#nested function
def outer(fun_name):
    def inner():
        print("This is decorator")
        fun_name()
    return inner
def ord_fun():
    print("this is ordinary function")

#ord_fun()

#calling nested func
decor=outer(ord_fun)
decor()






