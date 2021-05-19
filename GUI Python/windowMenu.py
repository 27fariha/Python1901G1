from tkinter import *



root=Tk()
menubar=Menu(root)

def donothing():
    filewin=Toplevel(root)
    btn=Button(filewin,text="Do Nothing")
    btn.pack()



#---------File Menu ------
filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="New",command=donothing)
filemenu.add_command(label="Open..",command=donothing)
filemenu.add_command(label="Save",command=donothing)
filemenu.add_command(label="Save as ..",command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Page Setup ..",command=donothing)
filemenu.add_command(label="Print ..",command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=donothing)

menubar.add_cascade(label="File",menu=filemenu)

#----End of File Menu ----

#----Edit Menu ----
editmenu=Menu(menubar,tearoff=0)






menubar.add_cascade(label="Edit",menu=editmenu)
#---End Edit MEnu ----
root.config(menu=menubar)
root.mainloop()