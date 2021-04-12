#key value pair
#Key = string
#value = depends on your data

students1={
    "Name": "abc",
    "Age":20,
    "batchcode":"1901g1",
    "year":2019,
   
}
print(students1)

#duplication
#students1={"year":2020}
#print(students1)

#list in dict
books={"books":["php","python","HTML","Css"]}
print(books)

#access
name=students1.get("Name")
print(name)

#all keys
keys=students1.keys()
print(keys)

#get value
value=students1.values()
print(value) 

#get item 
item=students1.items()
print(item)


if "Age1" in students1:
    print("Find")
else :
    print("Not Found")


#update value
students1["Age"]=30
print(students1)


#add key value
students1.update({"books":["php","python","HTML","Css"]})
print(students1)

#remove
#1
students1.pop("Age")
print(students1)

#2 
# last item
students1.popitem()
print(students1)

#3
del students1["Name"]
print(students1)

#4 all del
#del students1
#print(students1)


#clear all dict
#students1.clear()

#loops

students2={
    "Name": "Atif",
    "Age":20,
    "batchcode":"1901g1",
    "year":2019,
   
}

#get keys only
for x in students2:
    print(x)

for i in students2.keys():
    print(i)

#get values only
for a in students2:
    print(students2[a]) #students2[Name]

for i in students2.values():
    print(i)

# both key and value
for k , v in students2.items():
    print(k , v)

#nested  Dict
std={
    1:{
    "Name": "Atif",
    "Age":20,
    "batchcode":"1901g1",
    "year":2019, 
    },
    2:{
    "Name": "aneeq",
    "Age":20,
    "batchcode":"1901g1",
    "year":2019,
    },
    3:{
    "Name": "sufiyan",
    "Age":20,
    "batchcode":"1901g1",
    "year":2019,
    }
    
}

key = std.keys()

for i in std.keys():
    if i == 3:
        print(std[i])

    
        