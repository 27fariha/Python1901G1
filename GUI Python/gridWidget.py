import tkinter


root=tkinter.Tk()
colors= ['red','green','orange','white','yellow']
j=0
for clr in colors:
    tkinter.Label(text =clr , relief=tkinter.RIDGE,width="15").grid(row=j , column=0)
    tkinter.Entry(bg=clr, relief=tkinter.SUNKEN,width=10).grid(row=j,column=0)
    j=j+1
root.mainloop()


