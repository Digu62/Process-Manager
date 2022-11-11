import numpy as np
import tkinter as tk
from tkinter import *

import Process
from func_main import *

window = Tk()
window.title('Escalonador de Processos e Memória')
window.geometry("400x400")

lbl1 = Label(window, text='Número de processos', anchor='center')
lbl1.place(x=70, y=170)
ent1 = Entry(justify='center')
ent1.place(x=200, y=170)
        
lbl2 = Label(window, text='Quantum do sistema', anchor='center')
lbl2.place(x=70, y=200)
ent2 = Entry(justify='center')
ent2.place(x=200, y=200)

lbl3 = Label(window, text='Sobrecarga do sistema', anchor='center')
lbl3.place(x=70, y=230)
ent3 = Entry(justify='center')
ent3.place(x=200, y=230)

# ola, tem como dar commit pra eu testar a memoria já que eu não posso usar o terminal

def call_open():
    p = int(ent1.get())
    q = int(ent2.get())
    o = int(ent3.get())
    open_win(window,p,q,o)

btn1 = Button(window,text ="Avançar",command = call_open)
btn1.place(x=200, y=280)


window.mainloop()
