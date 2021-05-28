import tkinter

root=tkinter.Tk()
intv=tkinter.IntVar()
tkinter.Label(root,text="Select Gender",justify=tkinter.LEFT,padx=20).pack()
tkinter.Radiobutton(root,text="Male",padx=20,variable=intv,value=1).pack()
tkinter.Radiobutton(root,text="Female",padx=20,variable=intv,value=2).pack()
root.mainloop()