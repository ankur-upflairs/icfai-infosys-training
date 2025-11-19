import tkinter as tk
from tkinter import ttk,messagebox

root= tk.Tk()
def show_warning():
    messagebox.showinfo('Warning','You are not allowed')
    x=messagebox.askyesno('dkf','kdjf')
    print(x)
    
info = ttk.Button(root,text='show info',command=show_warning)
info.pack()
root.mainloop()





