from tkinter import *

root = Tk()
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side = BOTTOM)

buttom1 = Button(topFrame, text = "Button 1", fg = "red")


root.mainloop()
