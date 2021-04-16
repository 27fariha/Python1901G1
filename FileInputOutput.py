import os
import json
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
c.flush()
c.close()

#File Functions

#1. fileno()
c=open('test.txt','wb')
fid=c.fileno()
print("File Descriptor :", fid)
c.close()

#Isatty()
c=open('test.txt','wb')
ret=c.isatty()
print("Retunr Value :" , ret)
c.close()

#write file 
c=open('test.txt','w')
sen=c.write("Hello \n World")
c.close()

c=open('test.txt','r')
red=c.read(6)
print(red)

#sequence of data store
sequence1=["This \n","is\n","new File \n"]
c=open('test.txt','a')
c.writelines(sequence1)
c.close()


#saving data in objects
x,y,z=23,54,97                          #int
name = "abc"                            #string
std={'a':1,'b':2}                       #dic
friuts=["apple","Kiwi","Watermelon"]    #list

f=open("datafile.txt","w")
f.write(" %s , %s , %s " % (x,y,z))
f.write("\n %s \n"% name)
f.write(str(std)+"\n")
f.write(str(friuts)+'\n')
f.close()

#json objects
names=dict(first="abc",last="xyz")
record = dict( name = names ,job=["tester","Manager","CEO"],age=25)
print(record)

#dict convert into json => dumps

S=json.dumps(record)
print(S)
M=json.loads(S)
print(M)

#compare
print(M==S)

#store json into file
f=open("datafile.txt","a")
json.dump(record,f)
f.close()

#read json file
f=open("datafile.txt","r")
print(f.read())
f.close()
