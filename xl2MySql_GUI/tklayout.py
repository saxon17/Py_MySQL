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
L1.pack(ipadx = 200)

var1  = IntVar()
Entry(DeskWindow,textvariable=var1,).pack(expand = 1)

Label(L1,
      text = '-',
      bg = 'blue'
      ).pack(expand = 1,side = LEFT)

Label(L1,
      text = 'inside',
      bg = 'blue'
      ).pack(side = LEFT)


# var1  = IntVar()
# var2  = IntVar()

# entry1 = Entry(DeskWindow,textvariable=var1,).pack()
# entry2 = Entry(DeskWindow,textvariable=var2,).pa












L1 = LabelFrame(DeskWindow,text = '请输入检验批次、电表型号')
# 设置ipadx属性为20
L1.pack(ipadx = 100)
Label(L1,
      text = 'inside',
      bg = 'blue'
      ).pack(expand = 5,side = LEFT)

Label(L1,
      text = 'inside',
      bg = 'blue'
      ).pack(expand = 1,side = LEFT)

Label(L1,
      text = 'inside',
      bg = 'blue'
      ).pack(side = LEFT)




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