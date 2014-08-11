def Rename(OriginalName):
    	#	Rename

		if OriginalName =='Meter equipment identifier':
			return 'MEID'
		if OriginalName == 'Device Type':
			return  'DType'
		if OriginalName == 'Delivery Date':
		    return 'D_Date'        	
		if OriginalName ==	'Wasion Batch Number':
			return   'Wasion Batch'
		if OriginalName == 'SMSC Oder Number':
			return  'SMSC_Order_No'
		if OriginalName == 'Warranty To':
			return  'Warranty'
		if OriginalName == 'NCR Number':
			return  'NCR'
				
print Rename('Meter equipment identifier')