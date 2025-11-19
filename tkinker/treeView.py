import tkinter as tk
from tkinter import ttk,messagebox

root= tk.Tk()
root.geometry('600x400')
tree = ttk.Treeview(root,columns=('ID','Name',"Age"))
# tree['columns']=('ID','Name',"Age")
tree.pack(fill='both',expand=True)
tree.heading('ID',text='ID')
tree.heading('Name',text='Name')
tree.heading('Age',text='Age')
tree.column('#0',width=0,stretch=tk.NO)
tree.column('ID',width=80)
tree.column('Name',width=120,anchor='center')
tree.column('Age',width=100)
tree.insert('','end',values=(111,'Gagan',23))
tree.insert('','end',values=(112,'Pankaj',24))

root.mainloop()
#create a form with name and age 



