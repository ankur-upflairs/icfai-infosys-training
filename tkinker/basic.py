import tkinter as tk
from tkinter import ttk 

root = tk.Tk()
root.title('my first application')
root.geometry('600x400')
frame1=tk.Frame(root)
frame1.pack(fill='x')
frame2=tk.Frame(root,bg='green')
frame2.pack(fill='both' ,expand='True')
label = tk.Label(frame1,text='hello world!',bg='red',fg='blue',font=('TkDefault',20))
label.pack(side='left',expand='True',
        fill='both')
button = ttk.Button(frame1,text='click Me!')
button.pack(side='left',expand='True',pady=20)
btn2=tk.Button(frame2,text='tk button')
btn2.pack(side='left',expand='True',anchor='s')
root.resizable(0,1)
btn1=ttk.Button(frame2,text='button 2')
btn1.pack(side='left',expand='True')
root.mainloop()




