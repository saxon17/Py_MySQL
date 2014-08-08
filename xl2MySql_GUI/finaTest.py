# -*- coding: utf-8 -*-

import MySQLdb
import tkMessageBox
def Batchcreate(begin,end,var2,var3,var4,var5,text1,var8,var110): 
#(begin,end,DType,D_Date,WasionBatch,SMSC_Order_No,Remark)
	
			# 是否正常或者是否被清空
			
			#链接数据裤
			# Establish a MySQL connection 
			database = MySQLdb.connect (host="localhost", user = "saxon", passwd = "CcTqT29L4fwZ8pCs", db = "SMSC")
			# Get the cursor, which is used to traverse the database, line by line 
			cursor = database.cursor() 
			
			# Create the INSERT INTO sql query 
			# query = """INSERT INTO products_product(MEID,DType,Commu_Method,D_Date,Modem_IMEI,SIM_IMSI,SIM_ICC_id,IP_Address,Firmware_Version,
			# LLS_Secret,HLS_Secret,Authentication_Key,Encryption_Key)
			# VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

			query = """INSERT INTO products_product(MEID,DType,D_Date,WasionBatch,SMSC_Order_No,Remark,Warranty,SMSC_Order_No)
			VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""


			print query

			
			for i in range(begin,end+1):
				
						a = i 	#表号
						b = var2    #DType
						# c = sheet.cell(r,2).value 				#Commu_Method
						d = var3	#D_Date
						e = var4    #出厂批次
						f = var5 	#smsc order no.
						g = text1	#remark
						h = var8
						x = var110
						print '存入x值为:'+x
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
						values = (a,b,d,e,f,g,h,x)

						print values
						# Execute sql Query
						cursor.execute(query, values) 

			#	print "Mysql Error %d: %s" % (e.args[0], e.args[1])
			#	print "数据有误,请在excel中查找并修改提示中的重复或者错误项，再尝试重新插入数据！"

			
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
			
			




Batchcreate(7777777,7777777, 'var2', 'var3', 'var4', 'var5', 'text1', 'var8', 'vfuck')