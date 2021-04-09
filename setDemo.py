myset={"a","b","c","d","e"}
print(myset)

#constructor
myset1=set(("c","d","e","f","g"))
print(myset1)

#loop
for x in myset:
    print(x)

#check value
print("a" in myset)
check="a" in myset
print(check)

#add values
myset.add("f")
print(myset)

#print
#print(myset[5])

#add 2 sets
myset.update(myset1)
print(myset)

#remove
myset.remove("g")
print(myset)

myset.pop()
print(myset)

myset.pop()
print(myset)

#clear
#myset1.clear()
#print(myset1)

#type
print(type(myset))

#join
s3=myset.union(myset1)
print(s3)

s1={1,2,3,4,5}
s2={4,5,6,7,8}

#intersect
#1st method
s1.intersection_update(s2)
print(s1)

#2nd method
s4=s1.intersection(s2)
print(s4)


#not duplicate
s1.symmetric_difference_update(s2)
print(s1)

s5=s1.symmetric_difference(s2)
print(s5)