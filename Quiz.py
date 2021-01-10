import tkinter as tk
import tkinter.font as font
import random

window=tk.Tk(className=" Quiz Application")
window.option_add('*Font', '100')
window.geometry("500x500")
window['bg']='lightblue'

greeting = tk.Label(
    text="Quiz",
    fg="white",
    bg="black",
    width=5,
    height=1)
greeting.config(font=("Arial",45))
greeting.pack(padx=5,pady=5)

questions=['A','B','C','D','E']

random=random.randint(0,4)
number=questions[random]

question=tk.Label(text=number)
question.pack()

window.mainloop()