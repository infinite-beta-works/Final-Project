from tkinter import *
top = Tk()
top.title('Calendar')


#Size of the window
top.geometry("500x600")

#Drop Down Menu for Months
months = ['Jan','Feb','Mar','Apr','May','June','July','Aug','Sept','Oct','Nov','Dec'] #etc
variable_month = StringVar(top)
variable_month.set(months[0]) # default value
w1 = OptionMenu(top, variable_month, *months)
w1.place(x=150,y=20)
w1['state'] = 'normal'

#Drop Down Menu for Days
days = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31'] #etc
variable_day = StringVar(top)
variable_day.set(days[0]) # default value
w2 = OptionMenu(top, variable_day, *days)
w2.place(x=100,y=20)
w2['state'] = 'normal'

#Drop Down Menu for Years
years = ['2018','2019','2020'] #etc
variable_year = StringVar(top)
variable_year.set(years[0]) # default value
w3 = OptionMenu(top, variable_year, *years)
w3.place(x=210,y=20)
w3['state'] = 'normal'


#Second menu for long event

#Drop Down Menu for Months
months = ['Jan','Feb','Mar','Apr','May','June','July','Aug','Sept','Oct','Nov','Dec'] #etc
variable_month2 = StringVar(top)
variable_month2.set(months[0]) # default value
w4 = OptionMenu(top, variable_month2, *months)
w4.place(x=150,y=520)
w4['state'] = 'disabled'

#Drop Down Menu for Days
days = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31'] #etc
variable_day2 = StringVar(top)
variable_day2.set(days[0]) # default value
w5 = OptionMenu(top, variable_day2, *days)
w5.place(x=100,y=520)
w5['state'] = 'disabled'

#Drop Down Menu for Years
years = ['2018','2019','2020'] #etc
variable_year2 = StringVar(top)
variable_year2.set(years[0]) # default value
w6 = OptionMenu(top, variable_year2, *years)
w6.place(x=210,y=520)
w6['state'] = 'disabled'

#Creating an input for the user to name the event
e = Entry(top)
e.focus_set()
e.pack()

#Creating a label to give user information on the status of their date
label_1 = Label(top, text = ' ')
label_1.place(x=100,y=80)

#Creating a label to give user instructions for input
label_2 = Label(top, text = 'Type name of event here')
label_2.place(x=40,y=0)

def ok():
    valid_date = False
    value = ''
    
        
        
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
             
    #Enabling and disabling the buttons
    label_1['text'] = value
    value = ''
    ok_button['state']='disabled'
    confirm_date_button['state']='normal'
    change_date_button['state']='normal'
    long_event_button['state']='normal'
    e['state']='disabled'
    reset_calendar_button['state']='disabled'
    
    
#Button to confirm user's actions
ok_button = Button(top, text="OK", command = ok)
ok_button.place(x=100,y=50)

#function to get the user's date that they have chosen
def confirm_date():
    label_confirm = Label(top, text = 'Confirmed \n' 'The event ' + e.get() + ' occurs on ' + variable_month.get() + ' ' + variable_day.get() + ', ' + variable_year.get())
    label_confirm.place(x=100,y=275)
    
    #Writing dates to the file and storing them
    input_File = open("stored events.txt", 'a')
    input_File.write("IBW Scheduler\n")
    input_File.write(variable_month.get() + ' ' + variable_day.get() + ', ' + variable_year.get() + ' ' + e.get() +'\n')
    input_File.close()
    
    e['state']='normal'

#Button to confirm user's choice of date
confirm_date_button = Button(top, text="Continue With This Date", command = confirm_date)
confirm_date_button.place(x=100,y=100)
confirm_date_button['state']='disabled'


#Function to change the date by enabling and disabling various burronts
def change_date():
    ok_button['state']='normal'
    confirm_date_button['state']='disabled'
    change_date_button['state']='disabled'
    w1['state'] = 'normal'
    w2['state'] = 'normal'
    w3['state'] = 'normal'
    w4['state'] = 'disabled'
    w5['state'] = 'disabled'
    w6['state'] = 'disabled'
    reset_calendar_button['state']='normal'
    

#creating a button to change the date
change_date_button = Button(top, text="Change/New Date", command = change_date)
change_date_button.place(x=245,y=100)
change_date_button['state']='disabled'


def long_event():
    #Disabling and enabling the dropdown menus
    w1['state'] = 'disabled'
    w2['state'] = 'disabled'
    w3['state'] = 'disabled'
    w4['state'] = 'normal'
    w5['state'] = 'normal'
    w6['state'] = 'normal'
    confirm_long_event_button['state'] = 'normal'
    confirm_date_button['state']='disabled'
    reset_calendar_button['state']='disabled'
    
    
    
    
def print_event_period():   
    #Printing the statement
    valid_date = False
    value = ''
    value = 'The event ' + e.get() + ' lasts from ' + variable_month.get() + ' ' + variable_day.get() + ', ' + variable_year.get() + ' to ' + variable_month2.get() + ' ' + variable_day2.get() + ', ' + variable_year2.get()
        
    label_1 = Label(top, text = value)
    label_1.place(x=100,y=175)
    value = ''
    
    #Appending the event to an external file
    input_File = open("stored events", 'a')
    input_File.write("IBW Scheduler\n")
    input_File.write(variable_month.get() + ' ' + variable_day.get() + ', ' + variable_year.get() + ' to ' + variable_month2.get() + ' ' + variable_day2.get() + ', ' + variable_year2.get() + ' ' + e.get() +'\n')
    input_File.close()  
    
    #Enabling and disabling the buttons
    w1['state'] = 'normal'
    w2['state'] = 'normal'
    w3['state'] = 'normal'
    w4['state'] = 'disabled'
    w5['state'] = 'disabled'
    w6['state'] = 'disabled'
    e['state'] = 'normal'
    reset_calendar_button['state']='normal'
    
#Function to reset the file   
def reset():
    #Resetting the file to a blank state
    input_File = open("stored events.txt", 'w')
    input_File.write("")
    input_File.close()
    
#Function to enable the button to check the date for events
def pre_check_date():
    current_date = variable_month.get() + ' ' + variable_day.get() + ', ' + variable_year.get()
    
    #Resetting the file so that events can be checked more than once
    clear_file = open('search events by date.txt', 'w')
    clear_file.write('Here are the events from ' + current_date + '\n')
    clear_file.close
    
    #Enabling and disabling the buttons
    pre_check_date_button['state']='disabled'
    check_date_button['state']='normal'
    e['state'] = 'disabled'
    reset_calendar_button['state']='disabled'
    ok_button['state']='disabled'
    
#Function to read the file to check specific dates    
def check_date():
    current_date = variable_month.get() + ' ' + variable_day.get() + ', ' + variable_year.get()
    
    #Reading the contents of the file to find out what the user has already entered
    event_found = ''
    List = open("stored events.txt", 'r')
    List.readlines
    
    #Checking the file for events that match the user's reqeusted date
    for item in List:
        if current_date in item:
            #Writing the items that have the date the user specified to an external file
            print(item)
            write_to_file = open("search events by date.txt", 'a')
            write_to_file.write(item)
            write_to_file.close
            event_label = Label(top, text = 'Events have been written to an external file')
            event_label.place(x=175,y=275)            
    
    List.close() 
    
    #Enabling and disabling the buttons
    pre_check_date_button['state']='normal'
    e['state'] = 'normal'
    reset_calendar_button['state']='normal'
    ok_button['state']='normal'
    
#Button to resest the stored events    
reset_calendar_button = Button(top, text="Reset entire calendar", command = reset)
reset_calendar_button.place(x=100,y=215)
reset_calendar_button['state']='normal'

#Button for if the user has an event that last more than one day
long_event_button = Button(top, text="This event last longer than one day", command = long_event)
long_event_button.place(x=100,y=125)
long_event_button['state']='disabled'

#Button to confirm event period
confirm_long_event_button = Button(top, text="Confirm event period", command = print_event_period)
confirm_long_event_button.place(x=100,y=155)
confirm_long_event_button['state']='disabled'

#Button to unlock check date button
pre_check_date_button = Button(top, text="I have a date I want to check", command = pre_check_date)
pre_check_date_button.place(x=100,y=245)
pre_check_date_button['state']='normal'


#Button to inform user of events scheduled on specified date
check_date_button = Button(top, text="Check date", command = check_date)
check_date_button.place(x=100,y=275)
check_date_button['state']='disabled'


mainloop()
