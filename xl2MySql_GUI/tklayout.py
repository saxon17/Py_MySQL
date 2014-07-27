# -*- coding: utf-8 -*-
from Tkinter import *
DeskWindow = Tk()
# 改变root的大小为80x80
# DeskWindow.geometry('80x80+0+0')
print DeskWindow.pack_slaves()
# 创建三个Label分别使用不同的fill属性,改为水平放置
# 将第一个LabelFrame居左放置
L1 = LabelFrame(DeskWindow,text = '请输入批号')
# 设置ipadx属性为20
L1.pack()


var1  = IntVar()
var2  = IntVar()

entry1 = Entry(L1,textvariable=var1,).pack(side=LEFT)
lbB = Label(L1,text = '-').pack(side=LEFT)
entry2 = Entry(L1,textvariable=var2,).pack(side=LEFT)



# Label(L1,
#       text = '-',
#       bg = 'blue'
#       ).pack(expand = 1,side = LEFT)


# Label(L1,
#       text = 'inside',
#       bg = 'blue'
#       ).pack(side = LEFT)


# var1  = IntVar()
# var2  = IntVar()

# entry1 = Entry(DeskWindow,textvariable=var1,).pack()
# entry2 = Entry(DeskWindow,textvariable=var2,).pa












L2 = LabelFrame(DeskWindow,text = '请输入检验批次、电表型号')
L2.pack()
# 设置ipadx属性为20
var3  = IntVar()
var4  = IntVar()


Label(L2,text = '电表型号:').pack()

entry3 = Entry(L2,textvariable=var3,).pack()

Label(L2,text = '检验批次:').pack()

entry4 = Entry(L2,textvariable=var4,).pack()

# lbB = Label(L2,text = '电表型号:').pack(side=LEFT)

# entry2 = Entry(L2,textvariable=var4,).pack(side=LEFT)

# lbB = Label(L2,text = '电表型号:').pack(side=LEFT)

# entry2 = Entry(L2,textvariable=var4,).pack(side=LEFT)

# lbB = Label(L2,text = '电表型号:').pack(side=LEFT)

# entry2 = Entry(L2,textvariable=var4,).pack(side=LEFT)




# L2 = Label(DeskWindow,
#            text = 'pack2',
#            bg = 'blue'
#            ).pack(fill = BOTH,expand = 1,side = LEFT,padx = 10)
# L3 = Label(DeskWindow,
#            text = 'pack3',
#            bg = 'green'
#            ).pack(fill = X,expand = 0,side = LEFT,pady = 10)
print DeskWindow.pack_slaves()
DeskWindow.mainloop()