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
    x_position = 100
    y_position = 100

#Cria os labels de memoria
    lbl_main = Label(memory_window, text='Memória Principal', anchor='center')
    lbl_main.place(x=x_position - 10, y=y_position - 30)
    lbl_main.configure(bg='#569BAA')
    lbl_virt = Label(memory_window, text='Memória Vitual', anchor='center')
    lbl_virt.place(x=x_position * 3.9, y=y_position - 30) #Ainda não consegui montar esse label dinamico
    lbl_virt.configure(bg='#569BAA')

    main_memory = pd.DataFrame(index=np.arange(n_rows), columns=np.arange(2))
# Memoria principal
    for i in range(FirstHalf):
        for j in range(n_columns):
            main_memory.loc[i,j] = Entry(memory_window, width=3, fg='black',
                            font=('Arial',8,'bold'))
            if i <= (n_rows-SecondHalf)/2:
                main_memory.loc[i,j].grid(row=i, column=j)
            else:
                main_memory.loc[i,j].grid(row=i, column=j)
            main_memory.loc[i,j].insert(END,lst[i][j])

            if j == 0:
                 main_memory.loc[i,j].grid(padx=(x_position,0))

            if i == 0:
                main_memory.loc[i,j].grid(pady=(y_position,0))
            
            memory_window.update()

    for i in range(SecondHalf,n_rows):
        for j in range(n_columns):
            main_memory.loc[i,j] = Entry(memory_window, width=3, fg='black',
                            font=('Arial',8,'bold'))
            if i <= (n_rows-SecondHalf)/2:
                main_memory.loc[i,j].grid(row=i-SecondHalf, column=j+2) 
            else:
                main_memory.loc[i,j].grid(row=i-SecondHalf, column=j+2)

            main_memory.loc[i,j].insert(END,lst[i][j])

            if i == 25:
                main_memory.loc[i,j].grid(pady=(y_position,0))

    # Memoria virtual

    virtual_memory = pd.DataFrame(index=np.arange(n_rows), columns=np.arange(2))

    k = 5
    for i in range(FirstHalf): #rows
        for j in range(n_columns): # columns
            virtual_memory.loc[i,j] = Entry(memory_window, width=3, fg='black',
                            font=('Arial',8,'bold'))

            if j == 0:
                virtual_memory.loc[i,j].grid(row=i, column=j+k, padx=(300,0))
            else:
                virtual_memory.loc[i,j].grid(row=i, column=j+k )
            virtual_memory.loc[i,j].insert(END,lst[i][j])

            if j == 0:
                 virtual_memory.loc[i,j].grid(padx=(x_position + 100,0))

            if i == 0:
                virtual_memory.loc[i,j].grid(pady=(y_position,0))
    
    for i in range(SecondHalf,n_rows):
        for j in range(n_columns):
            virtual_memory.loc[i,j] = Entry(memory_window, width=3, fg='black',
                            font=('Arial',8,'bold'))

            virtual_memory.loc[i,j].grid(row=i-SecondHalf, column=j+k+2) 
            virtual_memory.loc[i,j].insert(END,lst[i][j])

            if i == 25:
                virtual_memory.loc[i,j].grid(pady=(y_position,0))

    pakcage = [memory_window, main_memory, virtual_memory]
    memory_window.mainloop()
    return pakcage

def processos_res(lista):
    window= Tk()
    window.title('Escalonador de Processos e Memória')
    window.geometry("800x800+0+0")
    window.configure(bg='#569BAA')
    window.iconbitmap('./images/icon.ico')

    window.mainloop()
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