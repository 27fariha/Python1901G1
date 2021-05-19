import tkinter

def show_entry():
    print("FirstName : %s \n LastName : %s" %(fname.get() , lname.get()))

root =tkinter.Tk()
tkinter.Label(root, text="First  Name ").grid(row=0)
tkinter.Label(root,text="Last Name").grid(row=1)
fname=tkinter.Entry(root)
lname=tkinter.Entry(root)
fname.grid(row=0 , column=1)
lname.grid(row=1,column=1)

tkinter.Button(root, text="Quit",command=root.quit).grid(row =3, column=0)
tkinter.Button(root,text="Show",command=show_entry).grid(row=3,column=1)
root.mainloop()