# -*- coding: utf-8 -*-
'''
from Tkinter import *
 #tkinter.messagebox

Deskwindow= Tk()
Deskwindow.title("SMSC ShipmentFile importer      v1.0")
Deskwindow.geometry('450x450+200+200')

labelText = StringVar()
labelText.set("Click button")
label1 = Label(Deskwindow,textvariable=labelText,height=4)
label1.pack()

checkBoxVal = IntVar()
checkBox1 = Checkbutton(Deskwindow,variable=checkBoxVal,text="Happy?")
checkBox1.pack()



Deskwindow.mainloop()
'''

from Tkinter import *


def about(): 
	w = Label(DeskWindow,text='''开发者感谢\nGitHub
		\npython\n



	作者博客http://blacksheepwall.sinaapp.com''')    
	w.pack(side=TOP)



def donothing():
   filewin = Toplevel(DeskWindow)
   button = Button(filewin, text="Do nothing button")
   button.pack()
   
DeskWindow = Tk()
menubar = Menu(DeskWindow)     #manubar是一个横着的菜单


#File键list设置

filemenu = Menu(menubar, tearoff=0)     #filemenu是一个竖着的菜单（casecade瀑布样）
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()


filemenu.add_command(label="Exit", command=DeskWindow.quit)
menubar.add_cascade(label="File", menu=filemenu) #File作瀑布样



#Edit菜单键设置
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)




#helpmenu
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)

DeskWindow.config(menu=menubar)
DeskWindow.mainloop()