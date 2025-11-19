import tkinter as tk
from tkinter import ttk 

root = tk.Tk()
root.title('my first application')
root.geometry('600x400')
var = tk.DoubleVar()
def getValue(event):
    print(var.get())
scale=ttk.Scale(root,orient='horizontal',
    from_=0 ,to=10 ,command=getValue ,
    variable=var)
scale.pack()
spinbox= ttk.Spinbox(root, from_=1 , to=20,
        wrap=True ,values=(5,10,15,20,25)  )
spinbox.pack()
def increment(event):
    print('clicked',spinbox.get())
spinbox.bind('<<Increment>>',increment)
def check():
    print('clicked')
checkbtn=ttk.Checkbutton(root,onvalue='on',
    offvalue='off', command=check)
checkbtn.pack()
root.mainloop()
