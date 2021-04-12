fruits = ["apple","banana","cherry","kiwi","mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

#comprehension 
#syntax [expression for item in existinglist ]

#copy list in a newlist
newlist1=[ x for x in fruits ]
print(newlist1)


# copy list that contain letter "a"
newlist2=[ x for x in fruits if "a" in x ]
print(newlist2)


#basic
for i in 'hello':
    print(i)

#comprehension
word=[i for i in 'hello']
print(word)

#if condition basic 
even=[even for even in range(20) if even%2==0]
print(even)

#Nested if 
nested =[y for y in range(100) if y%2==0 if y%5==0]
print(nested)


#to uppercase list
upperlist=[ x.upper() for x in fruits]
print(upperlist)

#set keyword
setkey=['fariha' for x in fruits]
print(setkey)

#print yur name
name=["aptech" for x in range(10)]
print(name)

#squre of the numbers
sqaure=[y*y for y in  range(16)]
print(sqaure)

#vowel 
sentence="This is aptech COmputer Education"
vowel =[i for i in sentence if i in 'aeiouAEIUO']
print(vowel)