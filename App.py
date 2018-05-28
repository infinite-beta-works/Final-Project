from tkinter import *
top = Tk()

top.geometry("500x500")

months = ['Jan','Feb','Mar','April','May','June','July','Aug','Sept','Oct','Nov','Dec']

variable_month = StringVar(top)
variable_month.set(months[0])

w = OptionMenu(top,variable_month,*months)
w.pack()

days = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29']

variable_day = StringVar(top)
variable_day.set(days[0])#Default Value

w = OptionMenu(top,variable_day,*days)
w.pack()

def ok():
    print("Value is: " + variable_month.get() + variable_day.get())
    value = variable_month.get() + " " + variable_day.get()
    label_1 = Label(top, text = value)
    label_1.pack()    

button = Button(top, text="OK", command = ok)
button.pack()





mainloop()