from tkinter import *
top = Tk()
#Size of the window
top.geometry("500x600")

#Drop Down Menu
months = ['Jan','Feb','Mar','Apr','May','June','July','Aug','Sept','Oct','Nov','Dec'] #etc


variable_month = StringVar(top)
variable_month.set(months[0]) # default value

w1 = OptionMenu(top, variable_month, *months)
w1.place(x=150,y=20)
w1['state'] = 'normal'

days = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31'] #etc

variable_day = StringVar(top)
variable_day.set(days[0]) # default value

w2 = OptionMenu(top, variable_day, *days)
w2.place(x=100,y=20)
w2['state'] = 'normal'

years = ['2018','2019','2020'] #etc

variable_year = StringVar(top)
variable_year.set(years[0]) # default value

w3 = OptionMenu(top, variable_year, *years)
w3.place(x=210,y=20)
w3['state'] = 'normal'

#Second menu for long event 
months = ['Jan','Feb','Mar','Apr','May','June','July','Aug','Sept','Oct','Nov','Dec'] #etc

variable_month2 = StringVar(top)
variable_month2.set(months[0]) # default value

w4 = OptionMenu(top, variable_month2, *months)
w4.place(x=150,y=520)
w4['state'] = 'disabled'

days = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31'] #etc

variable_day2 = StringVar(top)
variable_day2.set(days[0]) # default value

w5 = OptionMenu(top, variable_day2, *days)
w5.place(x=100,y=520)
w5['state'] = 'disabled'

years = ['2018','2019','2020'] #etc

variable_year2 = StringVar(top)
variable_year2.set(years[0]) # default value

w6 = OptionMenu(top, variable_year2, *years)
w6.place(x=210,y=520)
w6['state'] = 'disabled'

var1 = IntVar()


def ok():
    valid_date = False
    value = ''
    global var1
    reoccurring_event = Checkbutton(top, text="Reoccurring event", variable=var1)
    reoccurring_event.pack()
    reoccurring_event.place(x=100, y = 150)
    reoccurring_event.var = var1
    print(var1.get())
    if variable_month.get() == 'Apr' or variable_month.get() == 'June' or variable_month.get() == 'Sept' or variable_month.get() == 'Nov': # Checking to make sure months with 30 days are considered valid
        if variable_day.get() == '31':
            valid_date = False #Set validDate to False
        else:
            valid_date = True #Set validDate to True
    else:
        valid_date = True
        
    if variable_year.get() == '2020': #Fancy math to check whether it's a leap year.
        if variable_month.get() == 'Feb' and variable_day.get() == '30' or variable_day.get() == '31':
            valid_date = False #Set validDate to False
        else:
            valid_date = True #Set validDate to True        
    else:
        if variable_month.get() == 'Feb' and variable_day.get() == '29' or variable_day.get() == '30' or variable_day.get() == '31':
            valid_date = False #Set validDate to False
        else:
            valid_date = True #Set validDate to True         
            
    if valid_date == True:
        value = variable_month.get() + ' ' + variable_day.get() + ', ' + variable_year.get()
    else:
        value = 'Date is Invalid'
             
    label_1 = Label(top, text = value)
    label_1.place(x=100,y=80)
    value = ''
    ok_button['state']='disabled'
    confirm_date_button['state']='normal'
    change_date_button['state']='normal'
    long_event_button['state']='normal'
    

ok_button = Button(top, text="OK", command = ok)

ok_button.place(x=100,y=50)


def confirm_date():
    label_confirm = Label(top, text = 'Confirmed')
    label_confirm.place(x=100,y=175)
    global var1
    print (var1.get())
    

confirm_date_button = Button(top, text="Continue With This Date", command = confirm_date)

confirm_date_button.place(x=100,y=100)
confirm_date_button['state']='disabled'

def change_date():
    ok_button['state']='normal'
    confirm_date_button['state']='disabled'
    change_date_button['state']='disabled'    

change_date_button = Button(top, text="Change Date", command = change_date)

change_date_button.place(x=245,y=100)
change_date_button['state']='disabled'   

def long_event():
    w1['state'] = 'disabled'
    w2['state'] = 'disabled'
    w3['state'] = 'disabled'
    w4['state'] = 'normal'
    w5['state'] = 'normal'
    w6['state'] = 'normal'

long_event_button = Button(top, text="This event last longer than one day", command = long_event)
long_event_button.place(x=100,y=125)
long_event_button['state']='disabled'


mainloop()