# -*- coding: utf-8 -*-
'''import xlrd
file_location = "M:/av_py/mylove.xls"
workbook = xlrd.open_workbook(file_location)

sheet = workbook.sheet_by_index(0)
print sheet.cell_value(0, 0)
print sheet.nrows
print sheet.ncols

for c in range(sheet.ncols):
	print	sheet.cell_value(1, c)


data = [[sheet.cell_value(r,c) for c in range(sheet.ncols)] 
for r in range(sheet.nrows)]
print type(data)

print data[2][0]
'''


import xlrd 
import MySQLdb 
# Open the workbook and define the worksheet 
file_location = "C:/Users/SM/Desktop/shipment file(2600) V1.0.xls"
workbook = xlrd.open_workbook(file_location)
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
print ("I just imported  %3s columns and %3s rows  to MySQL!") % (columns,rows)