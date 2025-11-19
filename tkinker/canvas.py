import tkinter as tk
from tkinter import ttk
root=tk.Tk()
canvas=tk.Canvas(root,width=600,height=400,
        background='black'   )
canvas.pack()
line=canvas.create_line(0,0,300,200,
     fill='white'  )
rect= canvas.create_rectangle(150,50,300,100,
    outline='red')
canvas.create_oval(150,50,300,100,
    outline='yellow',width=5)
canvas.create_polygon(12,12,10,300,340,230,outline='blue')
canvas.create_arc(500,350,400,250,
    start=0,extent=90 ,fill='green',outline='red')
canvas.create_text(500,50,text='hello',fill='tan')
def move_rect():
    canvas.move(rect,0,20)
button=ttk.Button(root,text='move rect',
        command=move_rect)
button.pack()

root.mainloop()