count =0
while count < 3:
    count = count+1
    print(count)
#add else 
while count < 3:
    count = count+1
    print(count)
else:
    print("this is Else Block")
#for loop
n=4 # 1, 2,3,4
for i in range(0,4):
    print(i)

#odd num
for x in range(1,30,2):
    print(x)

#break loop
print("Break loop")
for x in range(1,30,2):
    if x == 15:
        break
    print(x)

#continue
print("Continue loop")
for x in range(1,30,2):
    if x == 15:
        continue
    print(x)

#print list in loop
mylist=["a","b","c","d",12,7.9,"e"]
for item in mylist:
    print(item)

#print tuple
mylist1=("a","b","c","d",12,7.9,"e")
for item in mylist1:
    print(item)