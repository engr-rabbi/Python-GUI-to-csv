## GUI Application data send to csv file ##


import tkinter as tk
from tkinter import ttk
import os
from csv import DictWriter

win=tk.Tk()
win.title("GUI Application")

# ******* Create Level *******#

UserLevel=ttk.Label(win, text='Name Enter: ')
UserLevel.grid(row=0,column=0, sticky=tk.W)

AgeLevel=ttk.Label(win, text='Enter your age: ')
AgeLevel.grid(row=1, column=0, sticky=tk.W)

GenderLevel=ttk.Label(win, text='Enter your Gender: ')
GenderLevel.grid(row=2, column=0, sticky=tk.W)

UserTypeLevel=ttk.Label(win, text='Your Type: ')
GenderLevel.grid(row=3, column=0, sticky=tk.W)

# ******* Create Entry Box *******#

UserVar=tk.StringVar()
UserEntry=ttk.Entry(win, width=16, textvariable=UserVar)
UserEntry.grid(row=0, column=1)

AgeVar=tk.StringVar()
AgeEntry=ttk.Entry(win, width= 16, textvariable=AgeVar)
AgeEntry.grid(row=1, column=1)


# ******* Create ComboBox *******#

GenderVer=tk.StringVar()
GenderCombobox=ttk.Combobox(win, width= 14, textvariable=GenderVer, state='readonly' )
GenderCombobox['value']=('Male', 'Female', "Other")
GenderCombobox.current(0)
GenderCombobox.grid(row=2, column=1)


# ******* Create ComboBox *******#

UserTypeVar=tk.StringVar()
UserRadioBt1=ttk.Radiobutton(win, text='Student', value='Student', variable=UserTypeVar)
UserRadioBt1.grid(row=4, column=0)

UserRadioBt2=ttk.Radiobutton(win, text="Teacher", value="Teacher", variable=UserTypeVar)
UserRadioBt2.grid(row=4, column=1)

# ******* Create Check button *******#

CheckVar=tk.IntVar()
CheckBt=ttk.Checkbutton(win, text="Send email for update", variable=CheckVar)
CheckBt.grid(row=5, columnspan=3, sticky=tk.W)

# ******* If want to store file in csv file ******* #

def action():
    UserName=UserVar.get()
    UserAge=AgeVar.get()
    UserGender=GenderVer.get()
    UserType=UserTypeVar.get()
    if CheckVar.get()==0:
        Subcription='No'
    else:
        Subscription="Yes"
    with open('file1.csv','a', newline='') as f:
        dict_writer=DictWriter(f,fieldnames=['User Name','Age','Gender','Type', 'Subscription1'])
        if os.stat('file1.csv').st_size==0:
            dict_writer.writeheader()
        dict_writer.writerow({
            'User Name':UserName,
            'Age':UserAge,
            'Gender':UserGender,
            'Type':UserType,
            'Subscription1': Subscription
        })

    UserEntry.delete(0,tk.END)
    AgeEntry.delete(0,tk.End)
    UserLevel.config(foreground='red')

# ******* Create Submit button *******#

SubmitBt=ttk.Button(win, text='Submit', command=action)
SubmitBt.grid(row=6,column=0, sticky=tk.E)
win.mainloop()