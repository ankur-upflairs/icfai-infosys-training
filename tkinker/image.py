import tkinter as tk
from tkinter import ttk,messagebox
from PIL import Image,ImageTk

root= tk.Tk()
img=Image.open('amir.jpeg').resize((64,48))
image=ImageTk.PhotoImage(img)
label= tk.Label(root,image=image,
    text='this is amir pic',compound='right')
label.pack()
root.mainloop()
#calculator , login , table Entry , pomodoro
#timer and converter app (degree to farenheite)
#form to listView add 




