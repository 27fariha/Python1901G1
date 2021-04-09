#1st method
fruits=("apple","watermelon","kiwi","cherry")
print(fruits)


#2nd method (constructor)
fruits1=tuple(("apple","watermelon","kiwi","cherry","kiwi"))
print(fruits1)

#access 
print(fruits[2])
print(fruits[1:3])
print(fruits[:3])
print(fruits[2:])

#check value
if "kiwii" not in fruits:
    print("Yes")
else :
    print("No")

if "kiwi"  in fruits:
    print("Yes")
else :
    print("No")

#add value in tuples
y=list(fruits)
y.append("orange")
fruits = tuple(y)
print(fruits)

#access through index num
for i in range(len(fruits)):
    print(fruits[i])

#join
fruits3=fruits + fruits1
print(fruits3)

#multipy
print("Multiply")
z=fruits*5
print(z)