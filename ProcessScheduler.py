import time
import Memory
import Process
import numpy as np
import VirtualMemory
import MemoryScheduler
from os import system, name
from time import sleep

import tkinter as tk
from tkinter import *
from tkinter import ttk

class ProcessScheduler:
    
    ExecutingProcess = None

    def __init__(self, Quantum, Overload,process_interface):
        self.Quantum = Quantum
        self.Overload = Overload
        self.process_window = process_interface[0]
        self.info_table = process_interface[1]
        self.progress_table = process_interface[2]
        self.step_buttom = process_interface[3]
        self.stop_buttom = process_interface[4]
        self.proceed_buttom = process_interface[5]
        self.var = process_interface[6]
        self.TurnAroundLabel = process_interface[7]

    def TurnAround(self, ProcessList):
        """The Turnaround is the time that the process wait to ending, counting
        his execution, the execution before he and other factors.

        Args:
            ProcessList (_type_): A list with process

        Returns:
            _type_: Returns the turnaround of the process list
        """
        Turnaround = 0
        for process in ProcessList:
            Turnaround += process.WaitTime + process.ExecutionTime
        self.TurnAroundLabel.config(text = "Turn Around = " + str(Turnaround/ProcessList.size) )
        return Turnaround/ProcessList.size

    # Escalonamento
    def FIFO(self, ProcessArray, MemAlgo):
        """This function implement the first in first out (FIFO) algorithm. 
        It's a no preemptive algorithm in which the CPU executes in order the process that arrive.

        Args:
            ProcessArray (Array): An array containing all the process in the instantiated.
        """

        CopyArray = np.array([]) 
        for process in ProcessArray: # copia pq python é so por referencia
            CopyArray = np.append(CopyArray, process.clone() )

        WorkingList = np.array(CopyArray) # lista de processos que serão executados, mas talvez ainda não esteja prontos
        TotalTime = 0 # conta o tempo decorrido
        ProcessCount = CopyArray.size
        ExecutingProcess = None #Process in execution   
        ReadyList = np.array([])

        MemScheduler = MemoryScheduler.MemoryScheduler() #Instancia um escalonador de memoria
        Mem = Memory.Memory()  #Instancia uma memoria real
        VMem = VirtualMemory.VirtualMemory(CopyArray) #Instancia uma memoria virtual

        #execuçao dos processos
        while ProcessCount != 0:
            
            for process in WorkingList: # so coloca na lista de prontos se já chegou
                if process.StartTime <= TotalTime:
                    ReadyList = np.append(ReadyList, process)
                    WorkingList = np.delete(WorkingList, np.where(WorkingList == process))
                    for i in range(TotalTime):
                        process.PrintList.append(" ")

            #Escolhe o proximo
            if ExecutingProcess == None: # so escolhe o proximo se nenhum estiver sendo executado
                for process in ReadyList:
                    if process.StartTime <= TotalTime: # escolhe o primeiro caso alguem ja tenho chegado
                        ExecutingProcess = process
                        # escolhendo algo de memoria
                        if MemAlgo == 1:
                            MemScheduler.FIFO(Mem, VMem, ExecutingProcess)
                        else:
                            MemScheduler.LRU(Mem, VMem, ExecutingProcess)
                        break

            TotalTime += 1

            #Ao executar um processo atualiza a janela
            if ExecutingProcess != None:
                self.progress_table.loc[int(ExecutingProcess.ProcessId),TotalTime-1].configure({"background":'Green'}) #Ao ler o processo marca ele como verde
                for process in ReadyList:
                    if process != ExecutingProcess:
                        self.progress_table.loc[int(process.ProcessId),TotalTime-1].configure({"background":'Grey'})
                self.process_window.update()

            try:
                ExecutingProcess.ExecutedTime += 1
                ExecutingProcess.PrintList.append("X")

                if ExecutingProcess.ExecutedTime == ExecutingProcess.ExecutionTime: # Remove o processo caso tenha terminado
                        ReadyList = np.delete(ReadyList, np.where(ReadyList == ExecutingProcess))
                        ExecutingProcess = None
                        ProcessCount -= 1
            except:
                pass

            #Tempo de espera para calculo de turnaround
            for process in ReadyList:
                if (process == ExecutingProcess) or (process.StartTime >= TotalTime):#não conta se é o que ta execuntado ou ainda "não chegou"
                    continue
                process.PrintList.append("O")
                process.WaitTime += 1

            for process in CopyArray:
                for i in range(process.WaitTime + process.ExecutedTime + process.StartTime ,TotalTime):
                    process.PrintList.append(" ")
            self.PrintProcess(CopyArray, TotalTime, Mem, VMem)
            
            if self.var.get() == 0:
                self.process_window.wait_variable(self.var)
        
        print("----------------------------------")

        print(f"Tempo total : {str(TotalTime)}")
        print("----------------------------------")
        

        print(f"Turnaround : {str(self.TurnAround(CopyArray))}")
        print("----------------------------------")
        return

    def Sjf(self, ProcessArray, MemAlgo):
        """This function implement the shortest job first algorithm
        It's a no preemptive algorithm in which the scheduler choses the process with the smallest execution time for the next execution.

        Args:
            ProcessArray (_type_): _description_
        """
        CopyArray = np.array([]) 

        for process in ProcessArray: # copia pq python é so por referencia
            CopyArray = np.append(CopyArray, process.clone() )

        WorkingList = np.array(CopyArray) # lista de processos que serão executados, mas talvez ainda não esteja prontos
        TotalTime = 0 # conta o tempo decorrido
        ProcessCount = CopyArray.size
        ExecutingProcess = None #processo no estado executando
        ReadyList = np.array([]) #lista de processos que chegaram e esperam sua vez

        inp = 'p'

        MemScheduler = MemoryScheduler.MemoryScheduler()

        Mem = Memory.Memory()
        VMem = VirtualMemory.VirtualMemory(CopyArray)

        #execuçao dos processos
        while ProcessCount != 0:

            for process in WorkingList: # so coloca na lista de prontos se já chegou
                if process.StartTime <= TotalTime:
                    ReadyList = np.append(ReadyList, process)
                    WorkingList = np.delete(WorkingList, np.where(WorkingList == process))
                    for i in range(TotalTime):
                        process.PrintList.append(" ")

            #Escolhe o proximo
            if ExecutingProcess == None: # so escolhe o proximo se nenhum estiver sendo executado
                for process in ReadyList:
                    if process.StartTime <= TotalTime : # so escolhe o proximo caso alguem ja tenho chegado
                        if ExecutingProcess == None: # escolhe o 1 para comparação
                            ExecutingProcess = process
                        else: # encontra o com menor job dos que ja chegaram
                            if process.ExecutionTime - process.ExecutedTime  < ExecutingProcess.ExecutionTime - ExecutingProcess.ExecutedTime:
                                ExecutingProcess = process

            if ExecutingProcess != None:
                # escolhendo algo de memoria
                if MemAlgo == 1:
                    MemScheduler.FIFO(Mem, VMem, ExecutingProcess)
                else:
                    MemScheduler.LRU(Mem, VMem, ExecutingProcess)

            TotalTime += 1
            #print("Tempo atual:" + str(TotalTime))
            #Ao executar um processo atualiza a janela
            if ExecutingProcess != None:
                print(f'TotalTime: {TotalTime}') #Codigo de debug
                print(f'ProcessId: {int(ExecutingProcess.ProcessId)}') #Codigo de debug
                self.progress_table.loc[int(ExecutingProcess.ProcessId),TotalTime-1].configure({"background":'Green'}) #Ao ler o processo marca ele como verde
                for process in ReadyList:
                    if process != ExecutingProcess:
                        self.progress_table.loc[int(process.ProcessId),TotalTime-1].configure({"background":'Grey'})
                self.process_window.update()
            
            try:
                ExecutingProcess.ExecutedTime += 1
                ExecutingProcess.PrintList.append("X")

                if ExecutingProcess.Deadline - (TotalTime - ExecutingProcess.StartTime) < 0:
                        self.progress_table.loc[int(ExecutingProcess.ProcessId),TotalTime-1].configure({"background":'Blue'}) #Ao ler o processo marca ele como cinza
                        self.process_window.update()
                        ExecutingProcess.MetDeadline = False

                if ExecutingProcess.ExecutedTime == ExecutingProcess.ExecutionTime: # Remove o processo caso tenha terminado
                        ReadyList = np.delete(ReadyList, np.where(ReadyList == ExecutingProcess))
                        ExecutingProcess = None
                        ProcessCount -= 1

            
            except:
                pass
            #Tempo de espera para calculo de turnaround
            for process in ReadyList:
                if (process == ExecutingProcess) or (process.StartTime >= TotalTime):#não conta se é o que ta execuntado ou ainda "não chegou"
                    continue
                process.PrintList.append("O")
                process.WaitTime += 1

                
            # for process in CopyArray:
            #     process.print_process()        
            # print("----------------------------")
            for process in CopyArray:
                for i in range(process.WaitTime + process.ExecutedTime + process.StartTime ,TotalTime):
                    process.PrintList.append(" ")
            
            self.PrintProcess(CopyArray, TotalTime, Mem, VMem)
            
            if self.var.get() == 0:
                self.process_window.wait_variable(self.var)

                
        print("----------------------------------")


        print(f"Tempo total : {str(TotalTime)}")
        print("----------------------------------")
        print(f"Turnaround : {str(self.TurnAround(CopyArray))}")
        print("----------------------------------")
        return

    def RoundRobin(self, ProcessArray, MemAlgo):
        """This function implement the round robin algorithm
        It's a preemptive algorithm in which time slices (quanta) are assigned to each process in equal portions and circular order.

        Args:
            ProcessArray (_type_): _description_
        """
        WorkingArray = np.array([]) # lista de processos que serão executados, mas talvez ainda não esteja prontos

        for process in ProcessArray: # copia pq python é so por referencia
            WorkingArray = np.append(WorkingArray, process.clone() )

        CopyArray = np.array(WorkingArray)

        ReadyList = np.array([]) # lista de prontos
        TotalTime = 0 # conta tempo decorrido
        ProcessCount = WorkingArray.size # qtd de processos a serem executados
        ExecutingProcess = None # processo no estado executando

        Overloading = False
        OverloadTime = self.Overload

        MemScheduler = MemoryScheduler.MemoryScheduler()

        Mem = Memory.Memory()
        VMem = VirtualMemory.VirtualMemory(CopyArray)
        #execuçao dos processos
        while ProcessCount != 0:

            for process in WorkingArray: # so coloca na lista de prontos se já chegou
                if process.StartTime <= TotalTime:
                    ReadyList = np.append(ReadyList, process)
                    WorkingArray = np.delete(WorkingArray, np.where(WorkingArray == process))
                    for i in range(TotalTime):
                        process.PrintList.append(" ")
            

            if ExecutingProcess == None: # escolhe o primeiro dos prontos se nenhum estiver sendo executado
                for process in ReadyList:
                    ExecutingProcess = process
                    # escolhendo algo de memoria
                    if MemAlgo == 1:
                        MemScheduler.FIFO(Mem, VMem, ExecutingProcess)
                    else:
                        MemScheduler.LRU(Mem, VMem, ExecutingProcess)
                    break

            TotalTime += 1

            # Executando
            if not Overloading:
                if ExecutingProcess != None:
                    self.progress_table.loc[int(ExecutingProcess.ProcessId),TotalTime-1].configure({"background":'Green'}) #Ao ler o processo marca ele como verde
                    for process in ReadyList:
                        if process != ExecutingProcess:
                            self.progress_table.loc[int(process.ProcessId),TotalTime-1].configure({"background":'Grey'})
                    self.process_window.update()

                try:
                    ExecutingProcess.ExecutedTime += 1
                    ExecutingProcess.ExecutionTimePerQuantum += 1
                    ExecutingProcess.PrintList.append("X")

                    if ExecutingProcess.ExecutedTime == ExecutingProcess.ExecutionTime: # Remove o processo caso tenha terminado
                            ReadyList = np.delete(ReadyList, np.where(ReadyList == ExecutingProcess))
                            ExecutingProcess = None
                            ProcessCount -= 1        

                    elif ExecutingProcess.ExecutionTimePerQuantum == self.Quantum and self.Overload > 0: # Chega se acabou o tempo dele 
                        ExecutingProcess.ExecutionTimePerQuantum = 0
                        Overloading = True        

                except:
                    pass

                #Tempo de espera para calculo de turnaround
                for process in ReadyList:
                    if (process == ExecutingProcess) or (process.StartTime >= TotalTime):#não conta se é o que ta execuntado ou ainda "não chegou"
                        continue
                    process.PrintList.append("O")
                    process.WaitTime += 1

            else:
                #print("Overloading")
                self.progress_table.loc[int(ExecutingProcess.ProcessId),TotalTime-1].configure({"background":'Red'}) #Ao ler o processo marca ele como vermelho
                for process in ReadyList:
                    if process != ExecutingProcess:
                        self.progress_table.loc[int(process.ProcessId),TotalTime-1].configure({"background":'Grey'})
                self.process_window.update()

                ReadyList = np.delete(ReadyList, np.where(ReadyList == ExecutingProcess))
                ReadyList = np.append(ReadyList, ExecutingProcess)

                
                for process in ReadyList:
                    if process.StartTime > TotalTime:#não sei se é necessario mas ta funcionando com
                        continue
                    process.PrintList.append("#")
                    process.WaitTime += 1
                OverloadTime -= 1
                
                if OverloadTime <= 0: # terminando overload
                    OverloadTime = self.Overload
                    ExecutingProcess = None
                    Overloading = False
              
            # for process in CopyArray:
            #     process.print_process()        
            # print("----------------------------")
            for process in CopyArray:
                for i in range(process.WaitTime + process.ExecutedTime + process.StartTime ,TotalTime):
                    process.PrintList.append(" ")
            
            self.PrintProcess(CopyArray, TotalTime, Mem, VMem)

            if self.var.get() == 0:
                self.process_window.wait_variable(self.var)

                
        print("----------------------------------")
        
        print(f"Tempo total : {str(TotalTime)}")
        print("----------------------------------")
        

        print(f"Turnaround : {str(self.TurnAround(CopyArray))}")
        print("----------------------------------")
        return

    def Edf(self, ProcessArray, MemAlgo):
        """This function implement the earliest deadline first algorithm
        It's a dynamic priority algorithm in which there's a priority queue based on the closeness to each process' deadline.
        Args:
            ProcessArray (_type_): _description_
        """
        WorkingArray = np.array([]) # lista de processos que serão executados, mas talvez ainda não esteja prontos

        for process in ProcessArray: # copia pq python é so por referencia
            WorkingArray = np.append(WorkingArray, process.clone() )

        CopyArray = np.array(WorkingArray)

        ReadyList = np.array([]) # lista de prontos
        TotalTime = 0 # tempo decorrido
        ProcessCount = WorkingArray.size
        ExecutingProcess = None # processo no estado executando

        Overloading = False
        OverloadTime = self.Overload

        MemScheduler = MemoryScheduler.MemoryScheduler()

        Mem = Memory.Memory()
        VMem = VirtualMemory.VirtualMemory(CopyArray)

        #execuçao dos processos
        while ProcessCount != 0:

            for process in WorkingArray:# so coloca na lista de prontos se já chegou
                if process.StartTime <= TotalTime:
                    ReadyList = np.append(ReadyList, process)
                    WorkingArray = np.delete(WorkingArray, np.where(WorkingArray == process))
                    for i in range(TotalTime):
                        process.PrintList.append(" ")

            if ExecutingProcess == None: # so escolhe o proximo se nenhum estiver sendo executado
                for process in ReadyList:
                    if process.StartTime <= TotalTime : # so escolhe o proximo caso alguem ja tenho chegado
                        if ExecutingProcess == None: # escolhe o 1 para comparação
                            ExecutingProcess = process
                        else: # encontra o deadline mais ceda dos que ja chegaram
                            if process.Deadline - (TotalTime - process.StartTime)  < ExecutingProcess.Deadline - (TotalTime - ExecutingProcess.StartTime):
                                ExecutingProcess = process

            if ExecutingProcess != None:
                # escolhendo algo de memoria
                if MemAlgo == 1:
                    MemScheduler.FIFO(Mem, VMem, ExecutingProcess)
                else:
                    MemScheduler.LRU(Mem, VMem, ExecutingProcess)

            TotalTime += 1

            # Executando
            if not Overloading:
                try:
                    ExecutingProcess.ExecutedTime += 1
                    ExecutingProcess.ExecutionTimePerQuantum += 1
                    ExecutingProcess.PrintList.append("X")


                    if ExecutingProcess != None:
                        self.progress_table.loc[int(ExecutingProcess.ProcessId),TotalTime-1].configure({"background":'Green'}) #Ao ler o processo marca ele como verde
                        for process in ReadyList:
                            if process != ExecutingProcess:
                                self.progress_table.loc[int(process.ProcessId),TotalTime-1].configure({"background":'Grey'})
                        self.process_window.update()
                    
                    if ExecutingProcess.Deadline - (TotalTime - ExecutingProcess.StartTime) < 0:
                        self.progress_table.loc[int(ExecutingProcess.ProcessId),TotalTime-1].configure({"background":'Blue'}) #Ao ler o processo marca ele como cinza
                        self.process_window.update()
                        ExecutingProcess.MetDeadline = False
                    # else:
                    #     print(f'TotalTime: {TotalTime}') #Codigo de debug
                    #     print(f'ProcessId: {int(ExecutingProcess.ProcessId)}') #Codigo de debug
                    #     self.progress_table.loc[int(ExecutingProcess.ProcessId),TotalTime-1].configure({"background":'Green'}) #Ao ler o processo marca ele como verde
                    #     self.process_window.update()

                    if ExecutingProcess.ExecutedTime == ExecutingProcess.ExecutionTime: # Remove o processo caso tenha terminado
                            ReadyList = np.delete(ReadyList, np.where(ReadyList == ExecutingProcess))
                            ExecutingProcess = None
                            ProcessCount -= 1        

                    elif ExecutingProcess.ExecutionTimePerQuantum == self.Quantum and self.Overload > 0:# Chega se acabou o tempo dele 
                        ExecutingProcess.ExecutionTimePerQuantum = 0
                        Overloading = True        

                except:
                    pass

                #Tempo de espera para calculo de turnaround
                for process in ReadyList:
                    if (process == ExecutingProcess) or (process.StartTime >= TotalTime):#não conta se é o que ta execuntado ou ainda "não chegou"
                        continue
                    process.PrintList.append("O")
                    process.WaitTime += 1
            else:
                #print("Overloading")
                if ExecutingProcess != None:
                    print(f'TotalTime: {TotalTime}') #Codigo de debug
                    print(f'ProcessId: {int(ExecutingProcess.ProcessId)}') #Codigo de debug
                    self.progress_table.loc[int(ExecutingProcess.ProcessId),TotalTime-1].configure({"background":'Red'}) #Ao ler o processo marca ele como vermelho
                    for process in ReadyList:
                        if process != ExecutingProcess:
                            self.progress_table.loc[int(process.ProcessId),TotalTime-1].configure({"background":'Grey'})
                    self.process_window.update()
                ReadyList = np.delete(ReadyList, np.where(ReadyList == ExecutingProcess))
                ReadyList = np.append(ReadyList, ExecutingProcess)

                
                for process in ReadyList:
                    if process.StartTime > TotalTime:#não sei se é necessario mas ta funcionando com
                        continue
                    process.PrintList.append("#")
                    process.WaitTime += 1
                OverloadTime -= 1
                if OverloadTime <= 0: # terminando overload
                    OverloadTime = self.Overload
                    ExecutingProcess = None
                    Overloading = False
                
              
            # for process in CopyArray:
            #     process.print_process()
            # print("----------------------------")
            for process in CopyArray:
                for i in range(process.WaitTime + process.ExecutedTime + process.StartTime ,TotalTime):
                    process.PrintList.append(" ")
            
            self.PrintProcess(CopyArray, TotalTime, Mem, VMem)

            if self.var.get() == 0:
                self.process_window.wait_variable(self.var)

                
        print("----------------------------------")

        print(f"Tempo total : {str(TotalTime)}")
        print("----------------------------------")
        

        print(f"Turnaround : {str(self.TurnAround(CopyArray))}")
        print("----------------------------------")
        return

    def PrintProcess(self,ProcessArray, TotalTime, Mem, VMem):
        #for i in range(TotalTime):
        # for windows
        if name == 'nt':
            _ = system('cls')
    
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')

       
        
        for process in ProcessArray:
            print(process.ProcessId, end = "")
            if process.StartTime < TotalTime:
                for j in range(TotalTime):
                    print(process.PrintList[j], end = "")
                if not process.MetDeadline:
                    print(" Estourou", end="")

            print()
        print()
        Mem.ShowMemory()
        VMem.ShowMemory()
        print("Legenda:")
        print("  X = Executando")
        print("  O = Esperando")
        print("  # = Overload")
        print("  Cada pagina na memoria possui 4096 de endereços assim a pagina n vai do endereço [n*4096,n*4096-1]")
        print()
        print()
        self.process_window.update_idletasks()
        time.sleep(1)
            
            

        return