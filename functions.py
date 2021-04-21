#create function
def my_function():
    print("This is some text")

#calling a function
my_function()


#argument 
def ShowName(name):
    print("Your name is :", name)

#calling a function with argument
ShowName("abc")


# passign 2 para
def add(num1 , num2):
    print("Add result is :",num1+num2)

#calling 
add(10,20)

#arbitrary argument

std ={"Aqib","imad","aliyan","atif"}

# def studentsList(std1,std2,std3,std4):
#     print("Students Names :",std1,std2,std3,std4)

# studentsList("atif","aqib","imad")

def studentsList(*std):
    print("Students List ",std[0],std[1])

studentsList("aqib","atif","imad")

#keyword value assign
def add1(num1,num2,num3):
    c=num1+num2+num3
    print(c)

add1(num1=29,num2=78,num3=20)


#json => arbitrary + keyword
def student(**std):
    print("Student name is : ",std["fname"],std["lname"])

#std=> multiple , * 
#std["key"]=> , **

student(fname="muhammad",lname="imad")


#by default function 
def country(country="null"):
    print(country)

country("pakistan")
country()

#list pass 
def listvalues(abc):
    for x in abc:
        print(x)


fruits=["apple","watermelon","kiwi","banana"]

listvalues(fruits)