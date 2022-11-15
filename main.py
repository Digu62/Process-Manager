from tkinter import *
from func_main import *

# processWindow()
# # memoryWindow()
# exit()

window = Tk()
window.title('Escalonador de Processos e Memória')
window.geometry("400x400+500+150")
window.resizable(height=False, width=False)
window.configure(bg='#569BAA')

lbl1 = Label(window, text='Número de processos', anchor='center')
lbl1.place(x=70, y=120)
ent1 = Entry(justify='center')
ent1.place(x=200, y=120)
lbl1.configure(bg='#569BAA')
        
lbl2 = Label(window, text='Quantum do sistema', anchor='center')
lbl2.place(x=70, y=150)
ent2 = Entry(justify='center')
ent2.place(x=200, y=150)
lbl2.configure(bg='#569BAA')

lbl3 = Label(window, text='Sobrecarga do sistema', anchor='center')
lbl3.place(x=70, y=180)
ent3 = Entry(justify='center')
ent3.place(x=200, y=180)
lbl3.configure(bg='#569BAA')

teachlbl = Label(window, text='Professor: Maycon')
teachlbl.place(x=0, y=312)
teachlbl.configure(bg='#569BAA')

discplbl = Label(window, text='Disciplina: Sistemas Operacionais')
discplbl.place(x=0, y=330)
discplbl.configure(bg='#569BAA')

teamlbl = Label(window, text='Equipe: Adrielle, Fernando, Igor, Rodrigo')
teamlbl.place(x=0, y=348)
teamlbl.configure(bg='#569BAA')

def call_open():
    p = int(ent1.get())
    q = int(ent2.get())
    o = int(ent3.get())
    open_win(window,p,q,o)

btn1 = Button(window,text ="Avançar",command = call_open)
btn1.place(x=170, y=230)


window.mainloop()
