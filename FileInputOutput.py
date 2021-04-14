import os
#write file
file1=open('test.txt','w') # by default read
file1.write('hello \n')
file1.write('world \n')
file1.close()

#read file
readfile=open('test.txt','r')
text=readfile.read()
print(text)

#get path 
print(os.getcwd())

#change file path
os.chdir('C:/Users/farihaahmed/Desktop')
print(os.getcwd())


#add text 
a=open('test.txt','w')
a.write("This is some text \n ")
a.write("This is second line of code \n")
a.close()

#append text in existing file
a=open('test.txt','a')
a.write('this is python code \n')
a.write('this is some text')
a.close()

#split word
a=open('test.txt')
#readlin=a.readlines()
#print(readlin)

splitword=a.read()
print(splitword)
print(splitword.split())

#convert into list
word=splitword.split()
print(type(word))
print(word[9])
a.close()

#read file in binary mode
b=open('test.txt','rb')
txt=b.read()
print(txt)
b.close()

#write file in binary 
c=open('test.txt','wb')
print("Name of File is :",c.name)