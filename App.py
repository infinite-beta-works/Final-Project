from tkinter import *
top = Tk()

#Size of the window
top.geometry("500x500")

#Drop Down Menu
months = ['Jan','Feb','Mar','Apr','May','June','July','Aug','Sept','Oct','Nov','Dec'] #etc

variable_month = StringVar(top)
variable_month.set(months[0]) # default value

w = OptionMenu(top, variable_month, *months)
w.place(x=150,y=20)

days = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31'] #etc

variable_day = StringVar(top)
variable_day.set(days[0]) # default value

w = OptionMenu(top, variable_day, *days)
w.place(x=100,y=20)

years = ['2018','2019','2020'] #etc

variable_year = StringVar(top)
variable_year.set(years[0]) # default value

w = OptionMenu(top, variable_year, *years)
w.place(x=210,y=20)



def ok():


    validDate = True
    
 
    if(int(variable_year.get()) % 4 == 0 and (int(variable_year.get()) % 100 != 0 or int(variable_year.get()) % 400 == 0)): #Fancy math to check wether it's a leap year.
        leapYear = True
    else:
        leapYear = False
    if(leapYear == True and variable_month.get() ==  "Feb" and int(variable_day.get()) >= 30):
            validDate = False
    elif(leapYear == False and variable_month.get() == "Feb" and int(variable_day.get()) >= 29):
        validDate = False
    if(validDate == True): 
        print ("Date is valid")
        value = variable_month.get() + ' ' + variable_day.get() + ', ' + variable_year.get()
        label_1 = Label(top, text = value)
        label_1.place(x=100,y=80)    
        value = ''
        ok_button['state']='disabled'
        confirm_date_button['state']='normal'
        change_date_button['state']='normal'
        
        
    else:
        print ("Date is invalid") 
        label_1 = Label(top, text = "Error")
        
        
ok_button = Button(top, text="OK", command = ok)
        
ok_button.place(x=100,y=50)

def confirm_date():
    validDate = True
    label_confirm = Label(top, text = 'Confirmed')
    label_confirm.place(x=100,y=130)

confirm_date_button = Button(top, text="Continue With This Date", command = confirm_date)
confirm_date_button.place(x=100,y=100)



def change_date():
    ok_button['state']='normal'
    confirm_date_button['state']='disabled'
    change_date_button['state']='disabled'    

change_date_button = Button(top, text="Change Date", command = change_date)

change_date_button.place(x=245,y=100)
change_date_button['state']='disabled'    

mainloop()