from tkinter import Label
windget = Label(None, text='hello')#none表示放在主窗口里面
windget.pack()#打包语句，缺省表示第一行居中
windget.mainloop()#巨大的无限循环，不停等待用户进行操作
