mylist=["Aqib","Atif","Aneeq","Imad","Aliyan","Aliyan",20,1.65]
print(mylist)
print(len(mylist))
print(type(mylist))
print(mylist[2])

# change value
mylist[3]="jaffar"
print(mylist)
#change value in a range
mylist[1:3]=["abc","xyz"]
print(mylist)

#remove from list
mylist.remove("Aliyan")
print(mylist)

# remove through index
mylist.pop(3)
print(mylist)

# remove last element5
mylist.pop()
print(mylist)

#del from list
del mylist[0]
print(mylist)

#clear from all 
#mylist.clear()
#print(mylist)

#append /insert 
mylist.append("Imad")
print(mylist)

#insert through index
mylist.insert(1,"intekhab")
print(mylist)

lista=["a","e","i","o","u"]
listb=["A","E","I","O","U"]

#append list
lista.extend(listb)
print(lista)





