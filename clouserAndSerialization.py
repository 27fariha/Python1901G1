import pickle
def outerFunc(x):
    def innerfunc():
        print(x)
    return innerfunc
    
obj=outerFunc(10) # outer param
obj() #inner

#delete outer func
del outerFunc

obj()


#using nonLocal Keyword
def OuterAb(x):
    result=0
    def InnerAB(n):
        nonlocal result
        while n > 0:
            result +=x*n  # result = result+x*n
            n-=1
        return result
    return InnerAB


myfun=OuterAb(7)
print(myfun(3))

#example
def counter_func():
    ctr=0
    def counting():
        nonlocal ctr
        ctr +=1
        return ctr
    return counting

count1=counter_func()
print(count1())  #1
print(count1())  #2
print(count1())  #3


count2=counter_func()
print(count2())  #1
print(count2())  #2


print(count1())  #4


#sets 
a=set("qwerty")
print(a)

b=set("banana")  # 6 character
print(b)

A={1,2,3,4}
B={1,2,3,4,5,6}

print(A==B)

#loop num 
for num in B:
    print(num)

#check in set
print(9 in A, 4 in B)


#add value in sets
A.add(5)
print(A)



#serializations
class Example:
    a_num=123
    a_string="Hello world"
    a_list=[1,2,3,4]
    a_dict={
        "Firstname": "Abc",
        "Lastname" : "Xyz",
        "Marks": [10,50,90]
    }
    a_tuple=(22,33,44,55)

my_obj=Example()

my_pickle_obj=pickle.dumps(my_obj)
print(f"Pickle Object : \n {my_pickle_obj}\n")

#unpickle
my_obj.a_dict=None

my_unpickle_obj=pickle.loads(my_pickle_obj)
print(f"Unpickle Object : \n {my_unpickle_obj.a_dict}\n")

