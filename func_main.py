import tkinter as tk
from tkinter import *

def open_win(window,p,q,o):

    newWindow = Toplevel(window)
    newWindow.title("Execução")
    newWindow.geometry("{}x{}".format(450+int((p-1)/10)*300,400+(p*70)))

    def multiple_yview(*args):
        txt1.yview(*args)
        txt2.yview(*args)
        btn.yview(*args)

    counter=0
    j=0
    for i in range(p):
        if counter==10:
            counter=0
            j+=1
        txt1 = Label(newWindow, text='Processo: {}'.format(i+1), font=17)
        txt1.place(x=150+j*300, y=((i+1-(j*10))*90))
        txt2 = Label(newWindow, text='Inicio do processo:')
        txt2.place(x=100+j*300, y=35+((i+1-(j*10))*90))

        btn = Entry(newWindow,justify='center')
        btn.place(x=220+j*300, y=35+((i+1-(j*10))*90))
        counter+=1
    