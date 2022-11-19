import math
import tkinter as tk
from tkinter import *
from tkinter import ttk
import time


class tempo:
    def clock():
        for i in range(1000000):
            pass
        return



window = Tk()
window.title('Escalonador de Processos e Memória')
window.geometry("800x800+500+150")
window.resizable(height=False, width=False)
window.configure(bg='#569BAA')




s = ttk.Style()
s.theme_use('clam')
s.configure("red.Horizontal.TProgressbar", foreground='red', background='red')





barra = ttk.Progressbar(
    window, 
    orient="horizontal",
    length=600, 
    mode="determinate",)
    
barra.place(x=70, y=150)




def go():
    for x in range(100):
        if x == 50:
            barra2 = ttk.Progressbar(
                window, 
                style="red.Horizontal.TProgressbar", 
                orient="horizontal",
                length=100, 
                mode="determinate", )
            barra2.place(x=370, y=150)
        elif x > 50:
            barra2['value'] += 10
        barra['value'] += 1
        window.update_idletasks()
        tempo.clock()
    return

button = Button(window, text="go", command=go)
button.place(x=80, y = 250)

window.mainloop()
