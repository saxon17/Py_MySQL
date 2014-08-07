#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os, sys
try:
    from tkinter import *
except ImportError:  #Python 2.x
    PythonVersion = 2
    from Tkinter import *
    from tkFont import Font
    from ttk import *
    #Usage:showinfo/warning/error,askquestion/okcancel/yesno/retrycancel
    from tkMessageBox import *
    #Usage:f=tkFileDialog.askopenfilename(initialdir='E:/Python')
    #import tkFileDialog
    #import tkSimpleDialog
else:  #Python 3.x
    PythonVersion = 3
    from tkinter.font import Font
    from tkinter.ttk import *
    from tkinter.messagebox import *
    #import tkinter.filedialog as tkFileDialog
    #import tkinter.simpledialog as tkSimpleDialog    #askstring()

class Application_ui(Frame):
    #这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('Search')
        self.master.geometry('453x422')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.style.configure('TFrame1.TLabelframe', font=('宋体',9))
        self.style.configure('TFrame1.TLabelframe.Label', font=('宋体',9))
        self.Frame1 = LabelFrame(self.top, text='Modify', style='TFrame1.TLabelframe')
        self.Frame1.place(relx=0.053, rely=0.057, relwidth=0.885, relheight=0.874)

        self.style.configure('TFrame2.TLabelframe', font=('宋体',9))
        self.style.configure('TFrame2.TLabelframe.Label', font=('宋体',9))
        self.Frame2 = LabelFrame(self.Frame1, text='choose the field you want to medify', style='TFrame2.TLabelframe')
        self.Frame2.place(relx=0.12, rely=0.087, relwidth=0.761, relheight=0.263)

        self.Combo1List = ['Add items in design or code!',]
        self.Combo1Var = StringVar(value='Add items in design or code!')
        self.Combo1 = Combobox(self.Frame2, text='Add items in design or code!', textvariable=self.Combo1Var, values=self.Combo1List, font=('宋体',9))
        self.Combo1.place(relx=0.105, rely=0.412, relwidth=0.79, relheight=0.206)
        self.Combo1Var.trace('w', self.Combo1_Change)

        self.Text1Var = StringVar(value='Text1')
        self.Text1 = Entry(self.Frame1, textvariable=self.Text1Var, font=('宋体',9))
        self.Text1.place(relx=0.2, rely=0.499, relwidth=0.601, relheight=0.176)
        self.Text1Var.trace('w', self.Text1_Change)

        self.style.configure('TCommand1.TButton', font=('宋体',9))
        self.Command1 = Button(self.Frame1, text='Modify修改', command=self.modifycmd, style='TCommand1.TButton')
        self.Command1.place(relx=0.2, rely=0.715, relwidth=0.601, relheight=0.22)

        self.style.configure('TLabel1.TLabel', anchor='w', font=('宋体',9))
        self.Label1 = Label(self.Frame1, text='请输入你要添加的值', style='TLabel1.TLabel')
        self.Label1.place(relx=0.2, rely=0.39, relwidth=0.601, relheight=0.068)


class Macation(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)

    def Combo1_Change(self, *args):
        #TODO, Please finish the function here!
        pass

    def Text1_Change(self, *args):  #modify value

      	pass

        

    def modifycmd(self, event=None):
        print self.Text1Var.get()

if __name__ == "__main__":
    top = Tk()
    Macation(top).mainloop()

