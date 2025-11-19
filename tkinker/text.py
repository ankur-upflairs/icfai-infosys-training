import tkinter as tk
from tkinter import ttk,messagebox

root= tk.Tk()

text= tk.Text(root,height=4)
text.pack(fill='both',expand=True,side='left')
text.insert('1.0','hello everyone')
# print(text.get('1.0','end'))
scroll = ttk.Scrollbar(root,orient='vertical'
    ,command=text.yview)
text['yscrollcommand']=scroll.set 
scroll.pack(side='right')
root.mainloop()
#create a form with name and age




