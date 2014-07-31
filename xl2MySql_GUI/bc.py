# -*- coding: utf-8 -*-
def Batchcreate(begin,end,b,d,e,f,g): #(begin,end,DType,D_Date,WasionBatch,SMSC_Order_No,Remark)
	
	
	#链接数据裤
	# Establish a MySQL connection 
	database = MySQLdb.connect (host="localhost", user = "saxon", passwd = "cccccc", db = "polldb")
	 # Get the cursor, which is used to traverse the database, line by line 
	cursor = database.cursor() 
	 # Create the INSERT INTO sql query 
	# query = """INSERT INTO products_product(MEID,DType,Commu_Method,D_Date,Modem_IMEI,SIM_IMSI,SIM_ICC_id,IP_Address,Firmware_Version,
	# LLS_Secret,HLS_Secret,Authentication_Key,Encryption_Key)
	# VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

	query = """INSERT INTO products_product(MEID,DType,D_Date,WasionBatch,SMSC_Order_No,Remark)
	VALUES (%s,%s,%s,%s,%s,%s)"""




	#存入数据
	try:
			for i in range(begin,end+1):
		
				a = i 	#表号
				b = var2    #DType
				# c = sheet.cell(r,2).value 				#Commu_Method
				d = var3	#D_Date
				e = var4    #出厂批次
				f = var5 	#smsc order no.
				g = var6	#remark

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
				values = (a,b,d,e,f,g)
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
			tkMessageBox.showinfo("showinfo demo","本次成功插入%3s个产品记录到数据库中!"% (end-began+1))

			print ("本次成功插入%3s个产品记录到数据库中!") % (end-began+1)
	

		
		
		
