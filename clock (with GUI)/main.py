from tkinter import *
from tkinter import ttk
import datetime
import time

def tiempo():
    fecha = datetime.datetime.now()

    hora = str(fecha).split(' ')[1]

    hora_final = str(hora).split('.')[0]

    display.config(text=hora_final)
    display.after(200, tiempo)

root = Tk()
root.geometry('500x100')
root.title('Clock')
display = Label(root, fg='red', font=('arial', 85))
display.pack()
tiempo()
root.mainloop()