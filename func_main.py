from tkinter import *

def open_win(window,p,q,o):

    newWindow = Toplevel(window)
    newWindow.title("Execução")
    newWindow.geometry("500x400")
    root= Tk()

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
    canvas.configura(yscrollcommand=scroll.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

    #segundo frame
    frame2 = Frame(canvas)
    #new frame -> canvas
    canvas.create_window((0,0), window=frame2, anchor='nw')


    counter=0
    j=0
    for i in range(p):
        if counter==10:
            counter=0
            j+=1
        Label(frame2, text=f'Processo(Id): {i}'.grid(row=i, column=0, pady=10, padx=10))
        Label(frame2, text='Inicio do processo:')
        Label(frame2, text='Tempo de execução:')
        Label(frame2, text='Deadline:')
        Label(frame2, text='Prioridade:')
        Label(frame2, text='Páginas na memória:')
        Entry(frame2,justify='center')
        counter+=1
        
    Button(frame2,text ="Avançar",command = '')



#def process_run(window, )
    #newWindow = Toplevel(window)
    #newWindow.title("Execução")
    #newWindow.geometry("{}x{}".format(450+int((p-1)/10)*300,400+(p*70)))