from tkinter import *

#winwow n widgets

win = Tk()  
def km_2_miles():
    
    miles = float(e1val.get()) * 1.6
    t1.insert(END, miles)


b1 = Button(win, text='Scan', command=km_2_miles)
# b1.pack()
b1.grid(row=0,column=0)

e1val = StringVar()
e1=Entry(win, textvariable=e1val)

e1.grid(row=0, column=1)

t1=Text(win, height=1,width=20)
t1.grid(row=0,column=2)

win.mainloop()

