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
file_location = "M:/av_py/mylove.xls"
workbook = xlrd.open_workbook(file_location)
sheet = workbook.sheet_by_index(0)
# Establish a MySQL connection 
database = MySQLdb.connect (host="localhost", user = "saxon", passwd = "cccccc", db = "mylove")
 # Get the cursor, which is used to traverse the database, line by line 
cursor = database.cursor() 
 # Create the INSERT INTO sql query 
query = """INSERT INTO mygf (name,major,star)
   VALUES (%s, %s, %s)"""
# Create a For loop to iterate through each row in the XLS file,
# starting at row 2 to skip the headers
for r in range(1, sheet.nrows):    # range(1,4) = [1,2,3]  从第一行到最后一行
	name = sheet.cell(r,0).value 
	major = sheet.cell(r,1).value     #cell(行,列) 
	star = sheet.cell(r,2).value
	# Assign values from each row 
	values = (name,major,star)
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