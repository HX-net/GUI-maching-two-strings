from tkinter import *
from tkinter import ttk # for GUI
from fuzzywuzzy import process 

win= Tk()

win.geometry("1000x250")

strOptions = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday",] #our database (for example days of the week) you can change it
weeks=("\nSaturday - Sunday - Monday - Tuesday - Wednesday - Thursday - Friday\n")
week = Label(win,text=weeks, font=("Helvetica 15 bold")) 
week.pack()#for show data in program
def display_text(): 
    global entry
    value= entry.get()
    Ratios = process.extract(value,strOptions)
    highest = list(process.extractOne(value,strOptions))
    string = f"\nmy guess is = {highest[0]} with this amount of percentage of compliance = {highest[1]}%\n\n\n"
    guest=Label(win, text=Ratios, font=("Courier 15 bold"))
    guest.pack()
    label.configure(text=string)

label=Label(win, text="", font=("Courier 15 bold"))
label.pack()

entry= Entry(win, width= 40 , font=("Helvetica 20 bold"))
entry.focus_set()
entry.pack()

ttk.Button(win, text= "test",width= 20, command= display_text).pack(pady=20)

win.mainloop()
