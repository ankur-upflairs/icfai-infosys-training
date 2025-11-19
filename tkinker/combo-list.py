import tkinter as tk
from tkinter import ttk 

root = tk.Tk()
root.title('my first application')
root.geometry('600x400')
var = tk.StringVar(value='A')
def show(event):
    print(var.get())
    # var.set('D')
combo= ttk.Combobox(root,
    values=('A','B','C','D') ,
    textvariable=var ,state='readonly')
combo.pack()
combo.bind('<<ComboboxSelected>>',show)
var1=tk.StringVar(value=('A','B','C'))
li= tk.Listbox(root,listvariable=var1)
# li["selectmode"]='extended'
li.pack()
def show1(event):
    i=li.curselection()[0]
    print(i,var1.get()[i])
   
li.bind('<<ListboxSelect>>',show1)
root.mainloop()