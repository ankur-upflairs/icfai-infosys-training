import tkinter as tk
from tkinter import ttk

root= tk.Tk()
root.geometry('600x400')
# frame1= tk.Frame(root)
# frame1.grid(row=0,column=0)
# frame2= tk.Frame(root)
# frame2.grid(row=1,column=0)
# frame3= tk.Frame(root)
# frame3.grid(row=2,column=0)
name_label=tk.Label(root,text='Name : ')
name_label.grid(row=0,column=0,sticky='w')
name=tk.StringVar()
pas=tk.StringVar()
def show():
    print(name.get(),pas.get())
name_entry=tk.Entry(root,textvariable=name)
name_entry.grid(row=0,column=1)
pass_label=tk.Label(root,text='Password : ')
pass_label.grid(row=1,column=0)
pass_entry=tk.Entry(root,textvariable=pas,show='*')
pass_entry.grid(row=1,column=1)
button=ttk.Button(root,text='Login',command=show)
button.grid(row=2,column=0,columnspan=2)

root.mainloop()

