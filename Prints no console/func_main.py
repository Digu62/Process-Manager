from tkinter import *
import math

def open_win(window,p,q,o):

    root= Tk()
    root.geometry('500x400')
    root.configure(bg='#569BAA')

    # frame
    main_frame = Frame(root)
    main_frame.pack(fill=BOTH, expand=1)

    #canvas 
    canvas = Canvas(main_frame)
    canvas.pack(side=LEFT, fill=BOTH, expand=1)

    #scroll
    scroll = Scrollbar(main_frame, orient=VERTICAL, command=canvas.yview)
    scroll.pack(side=RIGHT, fill=Y)


    #canvas config
    canvas.configure(yscrollcommand=scroll.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

    #segundo frame
    frame2 = Frame(canvas)
    #new frame -> canvas
    canvas.create_window((0,0), window=frame2, anchor='n')

    counter=0
    j=0
    for i in range(0,p):

        Label(frame2, text=f'Processo(Id): {i}').grid(row=j, column=0, sticky= N, pady=(0,7), padx=(0,20))    
        Entry(frame2, text=f'Processo(Id): {i}').grid(row=j, column=1, sticky= N, pady=(0,7), padx=(0,20))

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

    Button(frame2,text ="Avançar",command = '')

def memoryWindow():
    memory_window= Tk()
    memory_window.title('Escalonador de Processos e Memória')
    memory_window.geometry("800x800+300+0")
    memory_window.configure(bg='#569BAA')

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
            table.grid(row=i, column=j,padx=-1, pady=0) 
            table.insert(END,lst[i][j])

    for i in range(SecondHalf,n_rows):
        for j in range(n_columns):
            table = Entry(memory_window, width=3, fg='black',
                            font=('Arial',16,'bold'))

            table.grid(row=i-SecondHalf, column=j+2) 
            table.insert(END,lst[i][j])


    # Memoria virtual
    k = 5
    for i in range(FirstHalf): #rows
        for j in range(n_columns): # columns
            table = Entry(memory_window, width=3, fg='black',
                            font=('Arial',16,'bold'))

            if j == 0:
                table.grid(row=i, column=j+k, padx=(300,0) ) 
            else:
                table.grid(row=i, column=j+k ) 
            table.insert(END,lst[i][j])
    
    for i in range(SecondHalf,n_rows):
        for j in range(n_columns):
            table = Entry(memory_window, width=3, fg='black',
                            font=('Arial',16,'bold'))

            table.grid(row=i-SecondHalf, column=j+k+2) 
            table.insert(END,lst[i][j])

    
        
    memory_window.mainloop()


#def process_run(window, )
    #newWindow = Toplevel(window)
    #newWindow.title("Execução")
    #newWindow.geometry("{}x{}".format(450+int((p-1)/10)*300,400+(p*70)))