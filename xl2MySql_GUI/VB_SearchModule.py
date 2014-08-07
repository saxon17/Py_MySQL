# #!/usr/bin/env python
# #-*- coding:utf-8 -*-

# import os, sys
# try:
#     from tkinter import *
# except ImportError:  #Python 2.x
#     PythonVersion = 2
#     from Tkinter import *
#     from tkFont import Font
#     from ttk import *
#     #Usage:showinfo/warning/error,askquestion/okcancel/yesno/retrycancel
#     from tkMessageBox import *
#     #Usage:f=tkFileDialog.askopenfilename(initialdir='E:/Python')
#     #import tkFileDialog
#     #import tkSimpleDialog
# else:  #Python 3.x
#     PythonVersion = 3
#     from tkinter.font import Font
#     from tkinter.ttk import *
#     from tkinter.messagebox import *
#     #import tkinter.filedialog as tkFileDialog
#     #import tkinter.simpledialog as tkSimpleDialog    #askstring()

# class Application_ui(Frame):
#     #这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.master.title('Form1')
#         self.master.geometry('687x536')
#         self.createWidgets()

#     def createWidgets(self):
#         self.top = self.winfo_toplevel()

#         self.style = Style()

#         self.style.configure('TFrame1.TLabelframe', font=('宋体',9))
#         self.style.configure('TFrame1.TLabelframe.Label', font=('宋体',9))
#         self.Frame1 = LabelFrame(self.top, text='Frame1', style='TFrame1.TLabelframe')
#         self.Frame1.place(relx=0.105, rely=0.09, relwidth=0.689, relheight=0.226)

#         self.Combo1List = ['121111','22222','333333','444444','55555','66666','777777',]
#         self.Combo1Var = StringVar(value='11111,22222,33333')
#         self.Combo1 = Combobox(self.Frame1, text='Add items in design or code!', textvariable=self.Combo1Var, values=self.Combo1List, font=('宋体',9))
#         self.Combo1.place(relx=0.152, rely=0.264, relwidth=0.645, relheight=0.165)
#         self.Combo1Var.trace('w', self.Combo1_Change)	


# class Application(Application_ui):
#     #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
#     def __init__(self, master=None):
#         Application_ui.__init__(self, master)

#     def Combo1_Change(self, *args):
#         print 'i love you '
#         print self.Combo1.get()
#         # fuck = Tk()
#         # Application(fuck).mainloop()



#!/usr/bin/env python
#-*- coding:utf-8 -*-
import types
import MySQLdb
import os, sys
import tkMessageBox
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
        self.master.geometry('491x179')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.style.configure('TFrame1.TLabelframe', font=('宋体',9))
        self.style.configure('TFrame1.TLabelframe.Label', font=('宋体',9))
        self.Frame1 = LabelFrame(self.top, text='Chose you wanna update', style='TFrame1.TLabelframe')
        self.Frame1.place(relx=0.049, rely=0.089, relwidth=0.898, relheight=0.765)

        self.Combo1List = ['MEID','DType','Commu_Method',
            'D_Date','WasionBatch','SMSC_Order_No','Warranty','Remark']
        self.Combo1Var = StringVar(value='MEID')
        self.Combo1 = Combobox(self.Frame1, text='Add items in design or code!', textvariable=self.Combo1Var, values=self.Combo1List, font=('宋体',9))
        self.Combo1.place(relx=0.109, rely=0.467, relwidth=0.819, relheight=0.146)
        self.Combo1Var.trace('w', self.Combo1_Change)


class Application(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)

    def Combo1_Change(self, *args):
        #TODO, Please finish the function here!
        print 'i love you '
        print self.Combo1.get()

        SearchKey = self.Combo1.get()

        rooot = Toplevel()
                # root = Tk()
        frame1 = Frame(rooot)
        frame1.pack()
    

         #文件名输入  
  
        label1 = Label(frame1, text = "Search "+SearchKey+":")  
  
        

        var1 = StringVar()  #button按钮后，SearchUI里面的var1值变了，但这时候传过去的值已经是0
        var2 = StringVar()


          #MEID专用
        if SearchKey=="MEID":
               
            text1 = Entry(frame1,name = 'text1',textvariable=var1,width = 20)  
      
            text2 = Entry(frame1,name = 'mowei ',textvariable=var2,width = 20)  

            
      
            button2 = Button(frame1,text="Search",command=lambda:self.Search(SearchKey,text1.get(),text2.get()))  #CollectValueAndSearch(vari,var1,var2)  就在点击的一瞬间var1才的得到
      
            print text1.get()
            print text2.get()
       
      
            label1.pack(side=LEFT,padx=5)  
      
            text1.pack(side=LEFT, padx=2)   
            text2.pack(side=LEFT, padx=2)   
            button2.pack(side=LEFT, padx =5)  

        else:
            text1 = Entry(frame1,name = 'text1',width = 20)  
      
           
      
            button2 = Button(frame1,text="Search", )  
      
              
       
      
            label1.pack(side=LEFT,padx=5)  
      
            text1.pack(side=LEFT, padx=2)   
           
            button2.pack(side=LEFT, padx =5)  



        print 'UpdateValue: ' + SearchKey


    def Search(self,keyfield,a,b):
        # Establish a MySQL connection 
        database = MySQLdb.connect (host="localhost", user = "saxon", passwd = "CcTqT29L4fwZ8pCs", db = "SMSC")
        # Get the cursor, which is used to traverse the database, line by line 
        cursor = database.cursor() 

        # if type(a) is types.StringType: 
            
        #     print 'a now type is %s' %type(a)
        #     print 'b now type is %s ' %type(b)

        if (keyfield == "MEID"):
            query = '''select * from products_product
                             where %s BETWEEN %s and %s '''%(keyfield,a,b)
        
        else:

            query = '''select * from products_product
                             where keyfield = a'''
 


        #how many records
        count = cursor.execute(query)
             
             
        print type(count)


        print 'there has %s rows record' % count



        # def IfModify():
        ask = tkMessageBox.askokcancel('Do You Want To Modify Them',"共查找到%s个电表,是否需要对它们的某个数据项进行修改？" %count)
        if ask:
            # to do somethin  
            #Go to the Modify Module
            roooot = Toplevel()
            

            print("yes")
        else:
           # to do somethin
            print("no")




if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()




