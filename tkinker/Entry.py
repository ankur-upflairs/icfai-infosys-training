import tkinter as tk
from tkinter import ttk 

root = tk.Tk()
root.title('my first application')
root.geometry('600x400')
var=tk.StringVar()
entry= tk.Entry(root,textvariable=var)
entry.pack()
def getValue():
    print(var.get())
    var.set('changed')
    # print(entry.get())
    # entry.delete(0,'end')
    # entry.insert(0,'new')
btn= ttk.Button(root,text='get value',
                command=getValue)
btn.pack()
root.mainloop()