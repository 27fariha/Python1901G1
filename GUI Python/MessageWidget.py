import tkinter

top = tkinter.Tk()

message= "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries,"
w1=tkinter.Message(top, text = message)
w1.config(bg="green", font= ('times',16,'italic'))
w1.pack()

top.mainloop()