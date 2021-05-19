import tkinter

root=tkinter.Tk()
#label(rootvar , labelname1 , labelname2 ,.... )
w=tkinter.Label(root, text= "hello GUI Python Programming")
w.pack(side = "right")
w1=tkinter.Label(root, text= "hello GUI Python Programming 11111" )
w1.pack(side = "left")
root.mainloop()