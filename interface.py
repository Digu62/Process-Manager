import math
import pandas as pd
from time import sleep

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
        new_log_window(num_process,quantum,overload)
        # logs_window(window,num_process,quantum,overload)
        
    btn1 = Button(window,
                  text ="Avançar",
                  command = call_open)
    btn1.place(x=170, y=230)
    window.mainloop()

def logs_window(window,num_process,quantum,overload):
    
    print(f'Process: {num_process}')
    print(f'Quantum: {quantum}')
    print(f'Overload: {overload}')

    root= Tk()
    root.geometry('600x500+420+110')
    root.configure(bg='#569BAA')
    root.iconbitmap('./images/icon.ico')

    # frame
    main_frame = Frame(root)
    main_frame.pack(fill=BOTH, expand=1)
    main_frame.configure(bg='#569BAA')

    #canvas 
    canvas = Canvas(main_frame)
    canvas.pack(side=LEFT, fill=BOTH, expand=1)
    canvas.configure(bg='#569BAA')

    #scroll
    scroll = Scrollbar(main_frame, orient=VERTICAL, command=canvas.yview)
    scroll.pack(side=RIGHT, fill=Y)

    #canvas config
    canvas.configure(yscrollcommand=scroll.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

    #segundo frame
    frame2 = Frame(canvas)
    frame2.configure(bg='#569BAA')
    #new frame -> canvas
    canvas.create_window((0,0), window=frame2, anchor='n')

    j=0
    for i in range(0,num_process):

        Label(frame2, text=f'Processo(Id): {i}').grid(row=j, column=0, sticky= N, pady=(0,7), padx=(0,20))

        Label(frame2, text=f'Inicio do processo:').grid(row=j+1, column=0, sticky= N, pady=(0,7), padx=(0,20))  
        Entry(frame2, text='Inicio do processo:').grid(row=j+1, column=1, sticky= N, pady=(0,7), padx=(0,20))

        Label(frame2, text=f'Tempo de execução: {i}').grid(row=j+2, column=0, sticky= N, pady=(0,7), padx=(0,20))  
        Entry(frame2, text='Tempo de execução:').grid(row=j+2, column=1, sticky= N, pady=(0,7), padx=(0,20))

        Label(frame2, text=f'Deadline: {i}').grid(row=j+3, column=0, sticky= N, pady=(0,7), padx=(0,20))  
        Entry(frame2, text='Deadline:').grid(row=j+3, column=1, sticky= N, pady=(0,7), padx=(0,20))

        Label(frame2, text=f'Prioridade: {i}').grid(row=j+4, column=0, sticky= N, pady=(0,7), padx=(0,20))  
        Entry(frame2, text='Prioridade:').grid(row=j+4, column=1, sticky= N, pady=(0,7), padx=(0,20))

        Label(frame2, text=f'Páginas na memória: {i}').grid(row=j+5, column=0, sticky=N, pady=(0,60), padx=(0,20))  
        Entry(frame2, text='Páginas na memória:').grid(row=j+5, column=1, sticky=N, pady=(0,60), padx=(0,20))
        j=j+6

    btn1 = Button(canvas,text ="Avançar", command = processWindow)  
    btn1.place(x=300, y=20)

def new_log_window(num_process,quantum,overload):
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
        # process.get()
        # memory.get()
        # num_process,quantum,overload
        mem_algorithm = memory.get()
        process_algorithm = process.get()
        processWindow(num_process, quantum, overload, process_data, mem_algorithm, process_algorithm)
    proceed = Button(root,text ="Avançar", command = passing_data)
    proceed.place(x=x_position + 100, y=y_position + 330)

def memoryWindow():
    memory_window= Tk()
    memory_window.title('Escalonador de Processos e Memória')
    memory_window.geometry("800x800+0+0")
    memory_window.configure(bg='#569BAA')
    memory_window.iconbitmap('./images/icon.ico')

    # code for creating table
    n_rows = 50 #Will receive this values
    n_columns = 2 #Will receive this values
    counter = 0

    lst = []
    
    for i in range(n_rows):
        insert = []
        for j in range(n_columns):
            if j == 0:
                insert.append(counter)
            else:
                insert.append(" ")
        lst.append(insert)
        counter += 1
    
    FirstHalf = math.floor(n_rows/2)
    SecondHalf = math.ceil(n_rows/2)


    # Memoria principal
    for i in range(FirstHalf):
        for j in range(n_columns):
            table = Entry(memory_window, width=3, fg='black',
                            font=('Arial',16,'bold'))
            if i <= (n_rows-SecondHalf)/2:
                table.grid(row=i, column=j) 
            else:
                table.grid(row=i, column=j) 
            # , pady=(20),padx=(20), sticky=E
            table.insert(END,lst[i][j])

    for i in range(SecondHalf,n_rows):
        for j in range(n_columns):
            table = Entry(memory_window, width=3, fg='black',
                            font=('Arial',16,'bold'))
            if i <= (n_rows-SecondHalf)/2:
                table.grid(row=i-SecondHalf, column=j+2) 
            else:
                table.grid(row=i-SecondHalf, column=j+2) 
            # , pady=(0),padx=(0)
            table.insert(END,lst[i][j])


    # Memoria virtual
    k = 5
    for i in range(FirstHalf): #rows
        for j in range(n_columns): # columns
            table = Entry(memory_window, width=3, fg='black',
                            font=('Arial',10,'bold'))

            if j == 0:
                table.grid(row=i, column=j+k, padx=(300,0) ) 
            else:
                table.grid(row=i, column=j+k ) 
            table.insert(END,lst[i][j])
    
    for i in range(SecondHalf,n_rows):
        for j in range(n_columns):
            table = Entry(memory_window, width=3, fg='black',
                            font=('Arial',10,'bold'))

            table.grid(row=i-SecondHalf, column=j+k+2) 
            table.insert(END,lst[i][j])

    
    # processWindow()
    memory_window.mainloop()

# def processWindow(num_process, quantum, overload, process_data, mem_algorithm,process_algorithm):
def processWindow(): #Utilizado para testes 
    # Variaveis para teste
    # [init, exec, dead, pri, pag]
    process_data = {'0':[0,2,3,2,5], '1':[4,5,6,7,8], '2':[1,2,3,6,5],'3':[1,2,3,4,5],'4':[1,4,15,2,5], '5':[1,2,20,1,5], '6':[1,1,30,2,5]}
    num_process = len(process_data)
    mem_algorithm = 'FIFO'
    process_algorithm = 'Edf'
    quantum = 2
    overload = 1
    info_table = []
    # -------

    process_window = Tk()
    process_window.title('Escalonador de Processos')
    process_window.geometry("800x800+555+0")
    process_window.configure(bg='#569BAA')
    process_window.iconbitmap('./images/icon.ico')

#Table with process informations
    inf_x_space = 30
    inf_y_space = 100
    box_width = 2
    info_n_rows = num_process #Will receive number of process
    info_n_columns = 6 #Will receive time spend to compute all process
    info_table = pd.DataFrame(index=np.arange(info_n_rows), columns=np.arange(info_n_columns)) #Vai armazenar a tabela de grids

    # for i in range(info_n_rows):
    #     for j in range(info_n_columns):
    #         info_table.loc[i,j] = Entry(process_window, width=box_width, fg='black',
    #                     font=('Arial',16))
    #         if j == 0:
    #             info_table.loc[i,j].grid(row=i, column=j, padx=(inf_x_space,0))
    #             info_table.loc[i,j].insert(END, str(i))
    #         else:
    #             info_table.loc[i,j].grid(row=i, column=j)
    #             info_table.loc[i,j].insert(END,process_data[str(i)][j-1])

    #         if i ==0:
    #             info_table.loc[i,j].grid(row=i, column=j, pady=(inf_y_space,0))
            
    #         process_window.update()
    #         # info_table.configure({"background":'Green'})

    # #Insere os labels de forma dinamica na tabela de informações
    # labels = ['Id', 'St', 'Ex', 'Dl', 'Pr', "Mp"]
    # x = 0
    # for k in range(info_n_columns): #Instancia os labels
    #     lb = Label(process_window, text=str(labels[k]))
    #     x = x + box_width*15
    #     y = inf_y_space + box_width * info_n_rows * 15
    #     lb.place(x=x, y=y)#inf_y_space + box_width * info_n_rows + 10
    #     lb.configure(bg='#569BAA')


# Table o progress (Problemas quando plotada junto com a de infromações)
    progress_x_space = 200
    progress_y_space = inf_y_space
    progress_n_rows = num_process #Will receive number of process
    progress_n_columns = 50 #Will receive time spend to compute all process
    progress_table = pd.DataFrame(index=np.arange(progress_n_rows), columns=np.arange(progress_n_columns)) #Vai armazenar a tabela de grids
    
    for i in range(progress_n_rows):
        for j in range(progress_n_columns):
            progress_table.loc[i,j] = Entry(process_window, width=1, fg='black',
                        font=('Arial',16,'bold'))
            if j == 0:
                progress_table.loc[i,j].grid(row=i, column=j, padx=(progress_x_space,0))
            else:
                progress_table.loc[i,j].grid(row=i, column=j)

            if i ==0:
                progress_table.loc[i,j].grid(row=i, column=j, pady=(progress_y_space,0))
            # progress_table.configure({"background":'Green'})

    #Looping de exemplo para passagem do tempo nos processos
    # from time import sleep 
    # for k in range(30):
    #     progress_table.loc[0,k].configure({"background":'Green'})
    #     process_window.update()
    #     sleep(1)

# Creating ruller
    
#Creating step stop buttons
    step = Button(process_window,text =" > ", command = ())
    step.place(x=progress_x_space, y=progress_y_space - 30)

    stop = Button(process_window,text =" || ", command = ())
    stop.place(x=progress_x_space + 30, y=progress_y_space - 30)

    proceed = Button(process_window,text =" >> ", command = ())
    proceed.place(x=progress_x_space + 60, y=progress_y_space - 30)

#Após organizar a interface executa os processos
    #Instanciando os processos
    ProcessArray = [Process.process(process_data[str(i)][0],process_data[str(i)][1],process_data[str(i)][2],process_data[str(i)][3],process_data[str(i)][4],i) for i in range(num_process)]
    
    # print(objs)
    # for i in range(len(objs)):
    #     print(objs[i].ProcessId)

    mem = 0
    if mem_algorithm == "FIFO":
       mem = 1

    interface_package = [process_window, info_table, progress_table, step, stop, proceed]
    scheduler = ProcessScheduler(quantum,overload,interface_package)

    #---------------
    process_algorithm = 'Edf' #Utilizado para teste
    #---------------

    if process_algorithm == 'FIFO':
        scheduler.FIFO(ProcessArray, mem)
    elif process_algorithm == 'Sjf':
        scheduler.Sjf(ProcessArray, mem)
    elif process_algorithm == 'RoundRobin':
        scheduler.RoundRobin(ProcessArray, mem)
    elif process_algorithm == 'Edf':
        scheduler.Edf(ProcessArray, mem)
    
    
    
    
# ------------------------------------------------------------------------------------
#CODIGO QUE PROVAVELMENTE NÂO SERÀ UTILIZADO

# Creating progress bar
    # def val_bar(max):
    #     count = 0
    #     steps = max/100
    #     print(steps)
    #     while count < steps:
    #         count+=1
    #         i=0
    #         while i < 1000000: #Velocity from progress update
    #             i+=1
            
    #         if count == 50:
    #             progress_bar.config(style='red.Horizontal.TProgressbar')
    #         elif count == 80:
    #             progress_bar.config(style='green.Horizontal.TProgressbar')
    #         var_progress.set(count)
    #         process_window.update()


    # var_progress = DoubleVar()
    # st = ttk.Style()
    # st.theme_use('alt')
    # st.configure('red.Horizontal.TProgressbar', background='red')
    # st.configure('green.Horizontal.TProgressbar', background='green')
    # progress_bar = ttk.Progressbar(process_window, variable=var_progress, maximum=100, style='green.Horizontal.TProgressbar')
    # progress_bar.place(x=0,y=29,width=620,height=27) #grid(1) == width(40)
    # val_bar(100000)
#CODIGO QUE PROVAVELMENTE NÂO SERÀ UTILIZADO
# ------------------------------------------------------------------------------------
    process_window.mainloop()

def processos_res(lista):
    window= Tk()
    window.title('Escalonador de Processos e Memória')
    window.geometry("800x800+0+0")
    window.configure(bg='#569BAA')
    window.iconbitmap('./images/icon.ico')



    window.mainloop()