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
from FileDialog import *
import tkFileDialog
import xlrd 
import MySQLdb 
global PATH
PATH = ""





def import_xls():
	print "进入import"

	workbook = xlrd.open_workbook(PATH)




	sheet = workbook.sheet_by_index(0)
	# Establish a MySQL connection 
	database = MySQLdb.connect (host="localhost", user = "saxon", passwd = "cccccc", db = "shipment")
	 # Get the cursor, which is used to traverse the database, line by line 
	cursor = database.cursor() 
	 # Create the INSERT INTO sql query 
	query = """INSERT INTO shipmentfile(MEID,DType,Commu_Method,D_Date,Modem_IMEI,SIM_IMSI,SIM_ICC_id,IP_Address,Firmware_Version,
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

			# Assign values from each row 
			values = (a,b,c,d,e,f,g,h,i,j,k,l,m)
			# Execute sql Query
			cursor.execute(query, values) 

	except MySQLdb.Error,e:
			print "Mysql Error %d: %s" % (e.args[0], e.args[1])
			print "数据有误,请在excel中查找并修改提示中的重复或者错误项，再尝试重新插入数据！"

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
		print ("Just imported  %3s columns and %3s rows  to Datebase!") % (columns,rows)
		print ("本次成功插入%3s 列和 %3s 行数据到数据库中!") % (columns,rows)









def xopen():
	#fopen = tkFileDialog.askopenfile()
	#print type(fopen)
 	fileroute = tkFileDialog.askopenfilename()
 	PATH = fileroute
 	w = Label(DeskWindow,text='''
 %s 
 You are ready to drag data from this .xls file''' % fileroute)    
	w.pack(side=TOP)
#	print "%s字符串path" %PATH
	print PATH
	ROUTE = PATH
	ROUTE = ROUTE.replace('/','\\')
	str1 =  'r' + '"' + ROUTE + '"' 
#	print type(PATH)

	PATH = str1.encode('utf8')
	print PATH
	print type(PATH)
 	button1 = Button(DeskWindow,text='导入',command=import_xls)
	button1.pack()

	





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
#filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=xopen)
#filemenu.add_command(label="Save", command=donothing)
#filemenu.add_command(label="Save as...", command=donothing)
#filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()


filemenu.add_command(label="Exit", command=DeskWindow.quit)
menubar.add_cascade(label="File", menu=filemenu) #File作瀑布样


'''
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

'''


#helpmenu
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)

DeskWindow.config(menu=menubar)
DeskWindow.mainloop()