# -*- coding: utf-8 -*-
from Tkinter import *

def onclick():
	content = text.get("1.0","1.3").encode('utf8')
	
	if content == 'You':
		print ("Pls empity the  textarea")
   

root = Tk()
text = Text(root,width=40,height=10)
text.insert(INSERT, '''You can add remark here.
(if you do not want to remark,please make sure that this textarea is empty)
	如果不想添加remark，请用退格键或者delete清楚本文本框中的内容''')
# text.insert(END, "如果不想添加remark，请用退格键或者delete清楚本文本框中的内容")
text.pack()

text.tag_add("yellowtag", "1.0", "1.30")    #建立tag（头坐标，尾坐标）
text.tag_add("greenblacktag", "2.0", "3.40")
text.tag_config("yellowtag", background="yellow", foreground="blue")
text.tag_config("greenblacktag", background="black", foreground="green")


b = Button(root,text="printtext",command=onclick).pack()

root.mainloop()