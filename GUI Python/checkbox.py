import tkinter

def ShowValue():
    print("Yes : %d , \n No : %d"%(valueYes.get(),ValueNo.get()))



root=tkinter.Tk()
tkinter.Label(root,text="Your Choice :").grid(row=0,sticky=tkinter.W)
valueYes=tkinter.IntVar() # holds int values , default = 0
tkinter.Checkbutton(root, text="Yes",variable=valueYes).grid(row=1,sticky=tkinter.W)
ValueNo=tkinter.IntVar() # 0
tkinter.Checkbutton(root,text="No",variable=ValueNo).grid(row=2,sticky=tkinter.W)
tkinter.Button(root,text="show",command=ShowValue).grid(row=4)
root.mainloop()