from tkinter import *
import database

def get_selected_row(event):
    global row_selected
    index = list.curselection()[0]
    row_selected = list.get(index)
    e1.delete(0,END)
    e1.insert(END,row_selected[1])
    e2.delete(0, END)
    e2.insert(END, row_selected[2])
    e3.delete(0, END)
    e3.insert(END, row_selected[3])
    e4.delete(0, END)
    e4.insert(END, row_selected[4])
    e5.delete(0, END)
    e5.insert(END, row_selected[5])
    e6.delete(0, END)
    e6.insert(END, row_selected[6])

def view_command():
    list.delete(0,END)
    for row in database.view():
        list.insert(END,row)

def add_command():
    database.insert(date_text.get(), earning_text.get(), exercise_text.get(), study_text.get(), diet_text.get(), python_text.get())
    list.delete(0,END)
    list.insert(END,(date_text.get(), earning_text.get(), exercise_text.get(), study_text.get(), diet_text.get(), python_text.get()))

def search_command():
    list.delete(0, END)
    for row in database.search(date_text.get(), earning_text.get(), exercise_text.get(), study_text.get(), diet_text.get(), python_text.get()):
        list.insert(END, row)

def delete_command():
    database.delete(row_selected[0])

win = Tk()

win.wm_title('My application')

l1 = Label(win, text='Date')
l1.grid(row= 0, column= 0)

l2 = Label(win, text='Earnings')
l2.grid(row= 0, column= 2)

l3 = Label(win, text='Exercise')
l3.grid(row= 1, column= 0)

l4 = Label(win, text='Study')
l4.grid(row= 1, column= 2)

l5 = Label(win, text='Diet')
l5.grid(row= 2, column= 0)

l6 = Label(win, text='Python')
l6.grid(row= 2, column= 2)

date_text = StringVar()
e1 = Entry(win, textvariable= date_text)
e1.grid(row= 0, column=1)

earning_text = StringVar()
e2 = Entry(win, textvariable= earning_text)
e2.grid(row= 0, column=3)

exercise_text = StringVar()
e3 = Entry(win, textvariable= exercise_text)
e3.grid(row= 1, column=1)

study_text = StringVar()
e4 = Entry(win, textvariable= study_text)
e4.grid(row= 1, column=3)

diet_text = StringVar()
e5 = Entry(win, textvariable= diet_text)
e5.grid(row= 2, column=1)

python_text = StringVar()
e6 = Entry(win, textvariable= python_text)
e6.grid(row= 2, column=3)

list = Listbox(win, heigh=8, width=35)
list.grid(row=3, column=0, rowspan=9, columnspan=2)

sb =Scrollbar(win)
sb.grid(row=3, column=2,rowspan=9)

list.bind('<<ListboxSelect>>', get_selected_row)

b1 = Button(win, text='Add',width=12, pady=5, command= add_command)
b1.grid(row=3, column=3)

b2 = Button(win, text='Search',width=12, pady=5,command= search_command)
b2.grid(row=4, column=3)

b3 = Button(win, text='Delete date',width=12, pady=5, command= delete_command)
b3.grid(row=5, column=3)

b4 = Button(win, text='View all',width=12, pady=5, command= view_command)
b4.grid(row=6, column=3)

b5 = Button(win, text='Close',width=12, pady=5, command = win.destroy)
b5.grid(row=7, column=3)



win.mainloop()