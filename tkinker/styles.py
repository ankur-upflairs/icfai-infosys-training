import tkinter as tk
from tkinter import ttk,messagebox

root= tk.Tk()
root.geometry('600x400')
style= ttk.Style(root)
# print(style.theme_use())
# print(style.theme_names())
style.theme_use('clam') 
# print(style.theme_use())
button= ttk.Button(root,text=
                   "click me!")
button.pack()
print(button.winfo_class())
# print(style.layout('TButton'))
print(style.element_options('Button.label'))
style.configure('TButton',foreground='red')

root.mainloop()
#create a form with name and age



