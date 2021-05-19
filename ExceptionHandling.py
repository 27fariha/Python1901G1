#1
try:
    print("Hello")
except:
    print("name 'x' is not defined")
finally:
    print("Statement 1")
    print("Statement 2")
    print("Statement 3")



#3 else block
try:
    print("hello")
except:
    print("Error")
else:
    print("Statement 1")
    print("Statement 2")
    print("Statement 3")

#2
try:
    print(x)
    #catch(NullException ex)  , catch {}
except NameError:
    print("name 'x' is not defined")
finally:
    print("Statement 1")
    print("Statement 2")
    print("Statement 3")



#finally
f=open("test.txt","a") #read
try:
    f.write("Hello Worlddddddddddddddddddddddd")
except:
    print("Some Error")
finally:
    f.close()

#raise
x =1
if x<0:
    raise Exception("Not Allowed")

#2
x="hello"
if not type(x) is int:
    raise TypeError("Only Int Value allowed")