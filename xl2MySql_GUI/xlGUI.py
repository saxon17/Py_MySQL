
# -*- coding:utf-8 -*-
# file: TkinterCanvas.py
#
from Tkinter import *         # 导入Tkinter模块
from PIL import Image, ImageTk
import tkMessageBox
import tkFileDialog
import xlrd 
import MySQLdb 
global PATH
from playGround import Application

def textereaIsGood():
	content = text.get("1.0","1.3").encode('utf8')
	
	if content == 'You':
		return False
	else:
		return True

#messagebox
def ShowInfo():
	tkMessageBox.showinfo("showinfo demo", '''Thanks For GitHub&python\n



	Author's Blog: http://blacksheepwall.sinaapp.com''')
def mAbout():
	tkMessageBox.showinfo(title="About",message="you cicked New")
	return

def mShowWarning():
	tkMessageBox.showwarning("Attention",'''Please check the .xls file and make sure 
	the pattern is same as the shipmentfile v1.0!''')
	return

def mShowError():
	tkMessageBox.showerror("showerror demo", "Error")
	return
def mAsk():
	tkMessageBox.askokcancel("askokcancel demo", "OK?! CANCEL?!")
	return


#Real Function	

def donothing():
   win = Toplevel(DeskWindow)
   # button = Button(filewin, text="Do nothing button")
   # button.pack()
   
   Application(win )

def xopen():
	#fopen = tkFileDialog.askopenfile()
	#print type(fopen)
 	fileroute = tkFileDialog.askopenfilename()
 	global PATH
 	PATH = fileroute
 	

	a = tkMessageBox.askokcancel("Make sure then click OK",
	 "You are ready to drag data from the following .xls files %s" % fileroute)

	if a:
		import_xls()

  


def about(): 
	w = Label(DeskWindow,text='''开发者感谢\nGitHub
		\npython\n



	作者博客http://blacksheepwall.sinaapp.com''')    
	w.pack(side=TOP)

# def BulkCreate(began,end):
def Batchcreate(begin,end,var2,var3,var4,var5,text1,var8): 
#(begin,end,DType,D_Date,WasionBatch,SMSC_Order_No,Remark)
	
	if textereaIsGood():  #是否正常或者是否被清空
			
		#链接数据裤
		# Establish a MySQL connection 
		database = MySQLdb.connect (host="localhost", user = "saxon", passwd = "cccccc", db = "polldb")
		 # Get the cursor, which is used to traverse the database, line by line 
		cursor = database.cursor() 
		 # Create the INSERT INTO sql query 
		# query = """INSERT INTO products_product(MEID,DType,Commu_Method,D_Date,Modem_IMEI,SIM_IMSI,SIM_ICC_id,IP_Address,Firmware_Version,
		# LLS_Secret,HLS_Secret,Authentication_Key,Encryption_Key)
		# VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

		query = """INSERT INTO products_product(MEID,DType,D_Date,WasionBatch,SMSC_Order_No,Remark,Warranty)
		VALUES (%s,%s,%s,%s,%s,%s,%s)"""




		#存入数据
		try:
				for i in range(begin,end+1):
			
					a = i 	#表号
					b = var2    #DType
					# c = sheet.cell(r,2).value 				#Commu_Method
					d = var3	#D_Date
					e = var4    #出厂批次
					f = var5 	#smsc order no.
					g = text1	#remark
					h = var8
					# e = sheet.cell(r,4).value 				#Modem_IMEI
					# f = sheet.cell(r,5).value   #SIM_IMSI
					# g = sheet.cell(r,6).value 				#SIM_ICC_id
					# h = sheet.cell(r,7).value
					# i = sheet.cell(r,8).value
					# j = sheet.cell(r,9).value
					# k = sheet.cell(r,10).value
					# l = sheet.cell(r,11).value
					# m = sheet.cell(r,12).value
					# n = 					#WasionBatch
					# o = 					#SMSC_Order_No
					# p =						#Remark
					# Assign values from each row 
					# values = (a,b,,d,,,,,,,,,,n,o,p)
					values = (a,b,d,e,f,g,h)
					# Execute sql Query
					cursor.execute(query, values) 

		except MySQLdb.Error,e:
					tkMessageBox.showerror("Error", "数据有误,请在excel中查找并修改提示中的重复或者错误项，再尝试重新插入数据！")
					tkMessageBox.showerror("Error", "数据库中已存在该数据 %d: %s" % (e.args[0], e.args[1]) )
				#	print "Mysql Error %d: %s" % (e.args[0], e.args[1])
				#	print "数据有误,请在excel中查找并修改提示中的重复或者错误项，再尝试重新插入数据！"

		else:
				# Close the cursor
				cursor.close() 
				# Commit the transaction
				database.commit()
				# Close the database connection 
				database.close() 
				 # Print results
				print "" 
				print "All Done! Bye, for now." 
				print "" 
				
				#print "I just imported " %2B columns %2B " columns and " %2B rows %2B " rows to MySQL!" Hope this is useful. More to co
				tkMessageBox.showinfo("showinfo demo","本次成功插入%3s个产品记录到数据库中!"% (end-begin+1))

				print ("本次成功插入%3s个产品记录到数据库中!") % (end-begin+1)
	else:
		tkMessageBox.showerror("Error", "If you don't need remark,pls leave this erea empty."  )
		




#var1 为表号始
  #var3 DeviceType

  #var4为BatchNumber
  #texterea = Remark
  #var6 DeliveryDate
  #var7 NcrOderNum


def CollectValueAndBatchcreate():
	first = var1.get()
	last =	var2.get()
	dtype = var3.get()
	BatchNumber = var4.get()
	date = var6.get()
	ncr = var7.get()
	Warranty = var8.get()
	remark = text.get("1.0",END).encode('utf8')

	Batchcreate(first,last,dtype,date,BatchNumber,ncr,remark,Warranty)
# 	def Batchcreate(begin,end,var2,var3,var4,var5,text1): 
#                  (begin,end,DType,D_Date,WasionBatch,SMSC_Order_No,Remark)



def import_xls():
	print "进入import"
	global PATH

	workbook = xlrd.open_workbook(PATH )




	sheet = workbook.sheet_by_index(0)
	# Establish a MySQL connection 
	database = MySQLdb.connect (host="localhost", user = "saxon", passwd = "cccccc", db = "polldb")
	 # Get the cursor, which is used to traverse the database, line by line 
	cursor = database.cursor() 
	 # Create the INSERT INTO sql query 
	query = """INSERT INTO products_product(MEID,DType,Commu_Method,D_Date,Modem_IMEI,SIM_IMSI,SIM_ICC_id,IP_Address,Firmware_Version,
	LLS_Secret,HLS_Secret,Authentication_Key,Encryption_Key)
	VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
	# Create a For loop to iterate through each row in the XLS file,
	# starting at row 2 to skip the headers
	try:
		for r in range(1, sheet.nrows):    # range(1,4) = [1,2,..]  从第一行到最后一行
			a = sheet.cell(r,0).value 
			b = sheet.cell(r,1).value     #cell(行,列) 
			c = sheet.cell(r,2).value
			d = sheet.cell(r,3).value
			e = sheet.cell(r,4).value
			f = sheet.cell(r,5).value
			g = sheet.cell(r,6).value
			h = sheet.cell(r,7).value
			i = sheet.cell(r,8).value
			j = sheet.cell(r,9).value
			k = sheet.cell(r,10).value
			l = sheet.cell(r,11).value
			m = sheet.cell(r,12).value

			if (a == ""):
				a = None

			if (e == ""):
				e = None

			if (g == ""):
				g = None



			# if a = "":
			# 	a = None

			# if a = "":
			# 	a = None

				

			# Assign values from each row 
			values = (a,b,c,d,e,f,g,h,i,j,k,l,m)
			# Execute sql Query
			cursor.execute(query, values) 

	except MySQLdb.Error,e:
			tkMessageBox.showerror("Error", "数据有误,请在excel中查找并修改提示中的重复或者错误项，再尝试重新插入数据！")
			tkMessageBox.showerror("Error", "数据库中已存在该数据 %d: %s" % (e.args[0], e.args[1]) )
		#	print "Mysql Error %d: %s" % (e.args[0], e.args[1])
		#	print "数据有误,请在excel中查找并修改提示中的重复或者错误项，再尝试重新插入数据！"

	else:
		# Close the cursor
		cursor.close() 
		# Commit the transaction
		database.commit()
		# Close the database connection 
		database.close() 
		 # Print results
		print "" 
		print "All Done! Bye, for now." 
		print "" 
		columns = str(sheet.ncols)
		rows = str(sheet.nrows) 
		#print "I just imported " %2B columns %2B " columns and " %2B rows %2B " rows to MySQL!" Hope this is useful. More to co
		tkMessageBox.showinfo("showinfo demo","本次成功插入%3s 列和 %3s 行数据到数据库中!"% (columns,rows))

		print ("Just imported  %3s columns and %3s rows  to Datebase!") % (columns,rows)
		print ("本次成功插入%3s 列和 %3s 行数据到数据库中!") % (columns,rows)
















#GUI

DeskWindow = Tk()

DeskWindow.title ("made by Saxon")









#Batch
L1 = LabelFrame(DeskWindow,text = 'MEID')
# 设置ipadx属性为20
L1.pack()


var1  = IntVar()           #var1为批号头
var2  = IntVar()		   #var2为批号尾

entry1 = Entry(L1,textvariable=var1,).pack(side=LEFT)
lbB = Label(L1,text = '-').pack(side=LEFT)
entry2 = Entry(L1,textvariable=var2,).pack(side=LEFT)






L2 = LabelFrame(DeskWindow,text = '请输入检验批次、电表型号等')
L2.pack()
# 设置ipadx属性为20
var3  = StringVar()     #var3 DeviceType
var4  = StringVar()     #var4为BatchNumber
var5  = StringVar()		#texterea = Remark
var6  = StringVar()		#var6 DeliveryDate
var7  = StringVar()		#var7 NcrOderNum
var8  = StringVar()		#var8 Warranty

Label(L2,text = '      DeviceType:      ').pack(side=LEFT)

entry3 = Entry(L2,textvariable=var3,).pack(side=LEFT)    #var3为电表型号

# Label(L2,text = '检验批次:').pack()

# entry4 = Entry(L2,textvariable=var4,).pack()



L4 = LabelFrame(DeskWindow,text = '')
L4.pack()

Label(L4,text = '      DeliveryDate:    ').pack(side=LEFT)
entry4 = Entry(L4,textvariable=var6,).pack(side=LEFT)     #var6为D_Date









L5 = LabelFrame(DeskWindow,text = '')
L5.pack()

Label(L5,text = '    BatchNumber:     ').pack(side=LEFT)
entry4 = Entry(L5,textvariable=var4,).pack(side=LEFT)     #var4为BatchNumber


L7 = LabelFrame(DeskWindow,text = '')
L7.pack()
 
Label(L7,text = '        NCR No.:        ').pack(side=LEFT)
entry4 = Entry(L7,textvariable=var7,).pack(side=LEFT)     #var7为NCR No.

	

L8 = LabelFrame(DeskWindow,text = '')
L8.pack()
 
Label(L8,text = 'Warranty Period to: ').pack(side=LEFT)
entry8 = Entry(L8,textvariable=var8,).pack(side=LEFT)     #var7为NCR No.





L6 = LabelFrame(DeskWindow,text = '')
L6.pack()

# Label(L6,text = '      Remark:         ').pack(side=LEFT)
# entry5 = Entry(L6,textvariable=var5,).pack(side=LEFT)     #var4为Remark
text = Text(L6,width=38,height=5)
text.insert(INSERT, '''You can add remark here.
(if you do not want to remark,please make sure that this textarea is empty)如果不想添加remark，请用退格键或者delete清除本文本框中的内容''')
# text.insert(END, "如果不想添加remark，请用退格键或者delete清楚本文本框中的内容")
text.pack()

# text.tag_add("yellowtag", "1.0", "1.30")    #建立tag（头坐标，尾坐标）
# text.tag_add("greenblacktag", "2.0", "3.40")
# text.tag_config("yellowtag", background="yellow", foreground="blue")
# text.tag_config("greenblacktag", background="black", foreground="green")

bottomFrame = Frame(DeskWindow)  #底部站位框
bottomFrame.pack()
bottomLable = Label(bottomFrame,text='                                         ').pack(side=LEFT)
B1 = Button(bottomFrame,text='导入',fg='red',command=CollectValueAndBatchcreate).pack(side=LEFT)














menubar = Menu(DeskWindow)     #manubar是一个横着的菜单

#File键list设置

filemenu = Menu(menubar, tearoff=0)     #filemenu是一个竖着的菜单（casecade瀑布样）
#filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=xopen)
#filemenu.add_command(label="Save", command=donothing)
#filemenu.add_command(label="Save as...", command=donothing)
#filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()


filemenu.add_command(label="Exit", command=DeskWindow.quit)
menubar.add_cascade(label="File", menu=filemenu) #File作瀑布样




#Editmenu
Editmenu = Menu(menubar, tearoff=0)
Editmenu.add_command(label="Search", command=donothing)
Editmenu.add_command(label="Modify", command=donothing)
menubar.add_cascade(label="Search", menu=Editmenu)









#helpmenu
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Attention", command=mShowWarning)
helpmenu.add_command(label="About...", command=ShowInfo)
menubar.add_cascade(label="Help", menu=helpmenu)















DeskWindow.config(menu=menubar)









canvas = Canvas(DeskWindow,
    width = 500,      # 指定Canvas组件的宽度
    height = 400,      # 指定Canvas组件的高度
    bg = 'white')      # 指定Canvas组件的背景色
#im = Tkinter.PhotoImage(file='img.gif')     # 使用PhotoImage打开图片
image = Image.open("img.jpg")
im = ImageTk.PhotoImage(image)

canvas.create_image(250,180,image = im)      # 使用create_image将图片添加到Canvas组件中
canvas.create_text(302,340,       # 使用create_text方法在坐标（302，77）处绘制文字
   text = '''xls2MySQLv1.1 made by saxon
   			You can open your excel files 
   			from the file menue	'''      # 所绘制文字的内容
   ,fill = 'gray')       # 所绘制文字的颜色为灰色
canvas.create_text(300,340,
   text = '''xls2MySQLv1.1 made by saxon
   			You can open your excel files 
   			from the file menue	''',
   fill = 'black')
canvas.pack()         # 将Canvas添加到主窗口























DeskWindow.mainloop()






'''
from Tkinter import *
mGui = Tk()
mGui.geometry('500x500+300+100')
mGui.title("Be a man ")


canvas_1 = Canvas(mGui,height=300,bg="red",width=300)
canvas_1.pack()





mGui.mainloop()
#canvas
'''