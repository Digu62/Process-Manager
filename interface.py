import math
import pandas as pd
from time import sleep
import sys
from io import StringIO 

import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import Process
from ProcessScheduler import *


def main_window():
    #Criação da janela principal
    window = Tk()
    window.title('Escalonador de Processos e Memória')
    window.geometry("400x400+500+150")
    window.resizable(height=False, width=False)
    window.configure(bg='#569BAA')
    window.iconbitmap('./images/icon.ico')

    #Criação dos labels e campos
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
        num_process = int(ent1.get())
        quantum = int(ent2.get())
        overload = int(ent3.get())
        window.destroy()
        log_window(num_process,quantum,overload)
        
    btn1 = Button(window,
                  text ="Avançar",
                  command = call_open)
    btn1.place(x=170, y=230)
    window.mainloop()

def log_window(num_process,quantum,overload):
    print(f'Process: {num_process}')
    print(f'Quantum: {quantum}')
    print(f'Overload: {overload}')

    root= Tk()
    root.geometry('600x500+420+110')
    root.resizable(height=False, width=False)
    root.configure(bg='#569BAA')
    root.iconbitmap('./images/icon.ico')

    i = 0
    y_position = 70
    x_position = 150
    process_data = {}

    lb_id = Label(root, text=f'Processo(Id): {i}')
    lb_id.place(x=x_position, y=y_position)
    lb_id.configure(bg='#569BAA')

    lb_init = Label(root, text=f'Inicio do processo:')
    lb_init.place(x=x_position, y=y_position + 30)
    lb_init.configure(bg='#569BAA')
    init_entry = Entry(root, text='Inicio do processo:')
    init_entry.place(x=x_position + 120, y=y_position + 30)

    lb_exec = Label(root, text=f'Tempo de execução:')
    lb_exec.place(x=x_position, y=y_position + 60)
    lb_exec.configure(bg='#569BAA')
    exec_entry = Entry(root, text='Tempo de execução:')
    exec_entry.place(x=x_position + 120, y=y_position + 60)

    lb_dead   = Label(root, text=f'Deadline:')  
    lb_dead.place(x=x_position, y=y_position + 90)
    lb_dead.configure(bg='#569BAA')
    dead_entry = Entry(root, text='Deadline:')
    dead_entry.place(x=x_position + 120, y=y_position + 90)

    lb_pri = Label(root, text=f'Prioridade:')
    lb_pri.place(x=x_position, y=y_position + 120)
    lb_pri.configure(bg='#569BAA')
    pri_entry = Entry(root, text='Prioridade:')
    pri_entry.place(x=x_position + 120, y=y_position + 120)

    lb_pag = Label(root, text=f'Páginas na memória:')
    lb_pag.place(x=x_position, y=y_position + 150)
    lb_pag.configure(bg='#569BAA')
    pag_entry = Entry(root, text='Páginas na memória:')
    pag_entry.place(x=x_position + 120, y= y_position + 150)
        
    def all_filled():
        filled = False
        values = [  init_entry.get(), 
                    exec_entry.get(), 
                    dead_entry.get(), 
                    pri_entry.get(),  
                    pag_entry.get()]
        if "" not in values:
            print("Filled")
            filled = True

        return filled
    
    def clean_all():
        init_entry.delete(0, END)
        exec_entry.delete(0, END)
        dead_entry.delete(0, END)
        pri_entry.delete(0, END)
        pag_entry.delete(0, END)

    def next_process():
        nonlocal i
        if all_filled(): #Não altera os dados se algum dos campos estiver zerado
            if i < num_process: #Não excede o limite de processos
                process_data[str(i)] = [init_entry.get(), 
                                        exec_entry.get(), 
                                        dead_entry.get(), 
                                        pri_entry.get(),  
                                        pag_entry.get()] #Saves de data in dictionary
                
                i += 1
                if i < num_process: #Caso seja o ultimo valor não zera nem troca o id
                    lb_id.configure(text=f'Processo(Id): {i}')
                    clean_all()
                print(process_data)
        else:
            messagebox.showinfo(message="Preencha todos os campos")

    def prev_process():
        nonlocal i
        if i > 0:   #Não retorna menos que o minimo de processos
            i -= 1
            del process_data[str(i)] #Deleta o processo atual antes de voltar
            clean_all()
            lb_id.configure(text=f'Processo(Id): {i}')
            print(process_data)

    # btn1 = Button(root,text ="Avançar", command = processWindow)
    prev = Button(root,text ="<", command = prev_process)
    prev.place(x=x_position + 205, y=y_position + 175)

    next = Button(root,text =">", command = next_process)
    next.place(x=x_position + 225, y=y_position + 175)

    #Processos
    lb_process = Label(root, text='Escalonador de processos')
    lb_process.place(x=x_position, y=y_position + 230)
    lb_process.configure(bg='#569BAA')

    process = StringVar()
    process.set( "FIFO" )
    proc_menu = OptionMenu(root, process, "FIFO", "SJF", "Round Robin", "EDF")
    proc_menu.place(x=x_position + 150, y=y_position + 230)

    #Memoria
    lb_mem = Label(root, text='Escalonador de memoria')
    lb_mem.place(x=x_position, y=y_position + 280)
    lb_mem.configure(bg='#569BAA')

    memory = StringVar()
    memory.set( "FIFO" )
    mem_menu = OptionMenu(root, memory, "FIFO", "MRU")
    mem_menu.place(x=x_position + 150, y=y_position + 280)

    def passing_data():
        if len(process_data) != num_process: 
            messagebox.showinfo(message="Ainda faltam processos a serem cadastrados")
            return
        mem_algorithm = memory.get()
        process_algorithm = process.get()
        root.destroy()
        sheduler_window(num_process, quantum, overload, process_data, mem_algorithm, process_algorithm)
    proceed = Button(root,text ="Avançar", command = passing_data)
    proceed.place(x=x_position + 100, y=y_position + 330)

# def sheduler_window(num_process, quantum, overload, process_data, mem_algorithm,process_algorithm):
def sheduler_window(): #Utilizado para testes 
    # Variaveis para teste
    # [init, exec, dead, pri, pag]
    process_data = {'0':[2,4,35,0,1], '1':[3,2,15,0,1], '2':[6,7,20,0,1],'3':[9,8,25,0,1], '4':[1,8,25,0,1], '5':[2,8,25,0,1]}
    num_process = len(process_data)
    mem_algorithm = 'FIFO'
    process_algorithm = 'Edf'
    quantum = 2
    overload = 1
    info_table = []
    # -------

    #Global variables
    y_position = 40
    x_position = 200

    process_window = Tk()
    screen_width = process_window.winfo_screenwidth()
    screen_height = process_window.winfo_screenheight()
    process_window.title('Escalonador de Processos')
    process_window.geometry(f"{screen_width}x{screen_height}")
    process_window.configure(bg='#569BAA')
    #process_window.iconbitmap('./images/icon.ico')
    process_window.focus()

#Table with process informations
    box_width = 2
    info_n_rows = num_process #Will receive number of process
    info_n_columns = 6 #Will receive time spend to compute all process
    info_table = pd.DataFrame(index=np.arange(info_n_rows), columns=np.arange(info_n_columns)) #Vai armazenar a tabela de grids

    # for j in range(info_n_columns):
    #     for i in range(info_n_rows):
    #         info_table.loc[i,j] = Entry(process_window, width=box_width, fg='black',
    #                     font=('Arial',8))
    #         if i == 0:
    #             info_table.loc[i,j].grid(row=i, column=j, pady=(y_position,0))
    #             info_table.loc[i,j].insert(END, str(j))
    #         else:
    #             info_table.loc[i,j].grid(row=i, column=j)
    #             info_table.loc[i,j].insert(END,process_data[str(j)][i-1])
                

    #         if j ==0:
    #             info_table.loc[i,j].grid(row=i, column=j, padx=(x_position,0))

    # #Insere os labels de forma dinamica na tabela de informações
    # labels = ['Id', 'Start', 'Execution', 'Deadline', 'Priority', "Mem. Page"]
    # y = y_position
    # for k in range(info_n_rows): #Instancia os labels
    #     lb = Label(process_window, text=str(labels[k]), font=("Arial", 8))
    #     print(str(labels[k]))
    #     # y = y + box_width * info_n_rows * 15
    #     lb.place(x=x_position-80, y=y)#y_position + box_width * info_n_rows + 10
    #     y = y + 18
    #     lb.configure(bg='#569BAA')


# Table o progress (Problemas quando plotada junto com a de infromações)
    progress_y = y_position + 150
    progress_n_rows = num_process #Will receive number of process
    progress_n_columns = 50 #Will receive time spend to compute all process
    progress_table = pd.DataFrame(index=np.arange(progress_n_rows), columns=np.arange(progress_n_columns)) #Vai armazenar a tabela de grids
    
    for i in range(progress_n_rows):
        for j in range(progress_n_columns):
            progress_table.loc[i,j] = Entry(process_window, width=1, fg='black',
                        font=('Arial',16,'bold'))
            if j == 0:
                progress_table.loc[i,j].grid(row=i, column=j, padx=(x_position,0))
            else:
                progress_table.loc[i,j].grid(row=i, column=j)

            if i ==0:
                progress_table.loc[i,j].grid(row=i, column=j, pady=(progress_y,0))
        
    #Insere os labels de forma dinamica na tabela de progresso
    y = progress_y + 5
    for k in range(info_n_rows): #Instancia os labels
        lb = Label(process_window, text=str(k), font=("Arial", 8))
        lb.place(x=x_position-30, y=y)
        y = y + 28
        lb.configure(bg='#569BAA')
# Creating ruller
    
#Creating step stop buttons
    var = tk.IntVar()
    var.set(0)

    def Step():
        var.set(0)
        print("Working")
        return
    def Auto():
        var.set(1)
        return

    step = Button(process_window,text =" > ", command = Step)
    step.place(x=x_position, y=progress_y - 30)

    stop = Button(process_window,text =" || ", command = Step)
    stop.place(x=x_position + 30, y=progress_y - 30)

    proceed = Button(process_window,text =" >> ", command = Auto)
    proceed.place(x=x_position + 60, y=progress_y - 30)


#Creating a back buttom
    # def call_back(num_process, quantum, overload):
    #     log_window(num_process,quantum,overload)

    # back = Button(process_window,text =" < ", command = call_back(num_process, quantum, overload))
    # back.place(x=20, y=20)

#--------------------------------------------------------------------------------------------------------
#Instancia widjets da memoria
#     # code for creating table
#     n_rows = 50 #Will receive this values
#     n_columns = 2 #Will receive this values
#     counter = 0

#     lst = []
    
#     for i in range(n_rows):
#         insert = []
#         for j in range(n_columns):
#             if j == 0:
#                 insert.append(counter)
#             else:
#                 insert.append(" ")
#         lst.append(insert)
#         counter += 1
    
#     FirstHalf = math.floor(n_rows/2)
#     SecondHalf = math.ceil(n_rows/2)
#     x_position = 100

#     #Cria os labels de memoria
#     lbl_main = Label(process_window, text='Memória Principal', anchor='center')
#     lbl_main.place(x=x_position - 10, y=y_position - 30)
#     lbl_main.configure(bg='#569BAA')
#     lbl_virt = Label(process_window, text='Memória Vitual', anchor='center')
#     lbl_virt.place(x=x_position * 3.9, y=y_position - 30) #Ainda não consegui montar esse label dinamico
#     lbl_virt.configure(bg='#569BAA')

#     main_memory = pd.DataFrame(index=np.arange(n_rows), columns=np.arange(2))
# # Memoria principal
#     for i in range(FirstHalf):
#         for j in range(n_columns):
#             main_memory.loc[i,j] = Entry(process_window, width=3, fg='black',
#                             font=('Arial',8,'bold'))
#             if i <= (n_rows-SecondHalf)/2:
#                 main_memory.loc[i,j].grid(row=i, column=j)
#             else:
#                 main_memory.loc[i,j].grid(row=i, column=j)
#             main_memory.loc[i,j].insert(END,lst[i][j])

#             if j == 0:
#                  main_memory.loc[i,j].grid(padx=(0,0))

#             if i == 0:
#                 main_memory.loc[i,j].grid(pady=(y_position,0))
            
#             process_window.update()

#     for i in range(SecondHalf,n_rows):
#         for j in range(n_columns):
#             main_memory.loc[i,j] = Entry(process_window, width=3, fg='black',
#                             font=('Arial',8,'bold'))
#             if i <= (n_rows-SecondHalf)/2:
#                 main_memory.loc[i,j].grid(row=i-SecondHalf, column=j+2) 
#             else:
#                 main_memory.loc[i,j].grid(row=i-SecondHalf, column=j+2)

#             main_memory.loc[i,j].insert(END,lst[i][j])

#             if i == 25:
#                 main_memory.loc[i,j].grid(pady=(y_position,0))

#     # Memoria virtual

#     virtual_memory = pd.DataFrame(index=np.arange(n_rows), columns=np.arange(2))

#     k = 5
#     for i in range(FirstHalf): #rows
#         for j in range(n_columns): # columns
#             virtual_memory.loc[i,j] = Entry(process_window, width=3, fg='black',
#                             font=('Arial',8,'bold'))

#             if j == 0:
#                 virtual_memory.loc[i,j].grid(row=i, column=j+k, padx=(300,0))
#             else:
#                 virtual_memory.loc[i,j].grid(row=i, column=j+k )
#             virtual_memory.loc[i,j].insert(END,lst[i][j])

#             if j == 0:
#                  virtual_memory.loc[i,j].grid(padx=(x_position + 100,0))

#             if i == 0:
#                 virtual_memory.loc[i,j].grid(pady=(y_position,0))
    
#     for i in range(SecondHalf,n_rows):
#         for j in range(n_columns):
#             virtual_memory.loc[i,j] = Entry(process_window, width=3, fg='black',
#                             font=('Arial',8,'bold'))

#             virtual_memory.loc[i,j].grid(row=i-SecondHalf, column=j+k+2) 
#             virtual_memory.loc[i,j].insert(END,lst[i][j])

#             if i == 25:
#                 virtual_memory.loc[i,j].grid(pady=(y_position,0))

#Instanciando os processos
    #---------------
    memory_interface_package = [None,None,None]
    process_algorithm = 'FIFO' #Utilizado para teste
    #---------------

    ProcessArray = [Process.process(process_data[str(i)][0],process_data[str(i)][1],process_data[str(i)][2],process_data[str(i)][3],process_data[str(i)][4],i) for i in range(num_process)]
    mem = 0
    if mem_algorithm == "FIFO":
       mem = 1
    
    process_interface_package = [process_window, info_table, progress_table, step, stop, proceed, var]
    # memory_interface_package = [process_window, main_memory, virtual_memory]
    scheduler = ProcessScheduler(quantum,overload,process_interface_package, memory_interface_package)
    if process_algorithm == 'FIFO':
        scheduler.FIFO(ProcessArray, mem)
    elif process_algorithm == 'Sjf':
        scheduler.Sjf(ProcessArray, mem)
    elif process_algorithm == 'RoundRobin':
        scheduler.RoundRobin(ProcessArray, mem)
    elif process_algorithm == 'Edf':
        scheduler.Edf(ProcessArray, mem)
    
    process_window.mainloop()