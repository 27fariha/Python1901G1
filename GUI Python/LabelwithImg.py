import tkinter

root = tkinter.Tk()
img = tkinter.PhotoImage(file = "C:/Users/farihaahmed/Desktop/source.gif")
comment = """This is a general text used as a sample """
w1=tkinter.Label(root, image=img)
w2=tkinter.Label(root, text = comment)
w1.pack(side="right")
w2.pack(side ="left")

root.mainloop()