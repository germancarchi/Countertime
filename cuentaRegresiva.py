from ast import While
from itertools import count
import time

def cuentaRegresiva(t):
    while t:
        mins, secs = divmod(t, 60)
        contador = '{:02d}: {:02d}'.format(mins, secs)
        print (contador, end="\r" )
        time.sleep(1)
        t = t-1
    print ('Tiempo finalizado!!!')

t = input ("Ingrese el tiempo a cronometrar en segundos:  ")

cuentaRegresiva (int(t))

from tkinter import *

root = Tk()
root.title("Cuenta regresiva")
root.geometry("200x100")


label = Label(root, text = "Tiempo finalizado!!!")
label.grid(row=4, column=2)

root.mainloop()
