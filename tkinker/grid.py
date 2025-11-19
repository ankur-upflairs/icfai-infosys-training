import tkinter as tk
from tkinter import ttk 

root = tk.Tk()
root.title('my first application')
root.rowconfigure(0,weight=1)
root.columnconfigure(0,weight=1)
frame1=tk.Frame(root)
frame1.grid(row=0,column=0,sticky='nsew')
frame1.columnconfigure(0,weight=1)
frame1.columnconfigure(1,weight=1)

# frame2=tk.Frame(root,bg='green')
# frame2.pack(fill='both' ,expand='True')
label = tk.Label(frame1,text='hello world!',bg='red',fg='blue',font=('TkDefault',20))
label.grid(row=0,column=0 ,sticky='ew')
button = ttk.Button(frame1,text='click Me!')
button.grid(row=0,column=1,sticky='e')
# btn2=tk.Button(frame2,text='tk button')
# btn2.pack(side='left',expand='True',anchor='s')
# root.resizable(0,1)
# btn1=ttk.Button(frame2,text='button 2')
# btn1.pack(side='left',expand='True')
root.mainloop()




