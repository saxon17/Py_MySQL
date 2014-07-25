# -*- coding: utf-8 -*-
from Tkinter import *
def keyPress(a):
    l = list(entry1.get())
    for i in range(len(l) - 1, -1, -1):
        if not(48 <= ord(l[i]) <= 57 or ord(l[i]) == 46):
            entry1.delete(i, i+1)

def BounceLable():
	Btext = var1.get()    
	BLable = Label(root,text=Btext)
	BLable.pack()






root = Tk()
var1  = IntVar()
var2  = IntVar()

entry1 = Entry(root,textvariable=var1,)
entry2 = Entry(root,textvariable=var2,)


entry1.bind('<KeyRelease>', keyPress)
button1 = Button(root,text='open',command =BounceLable)
button1.pack()
# entry1.pack() 
# entry2.pack() 

entry1.grid(row= 0,column = 0)
entry2.grid(row=0,column = 2,columnspan = 2)



root.mainloop()
print  var1.get()