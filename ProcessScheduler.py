import Process
import numpy as np

class ProcessScheduler:
    
    ExecutingProcess = None

    def __init__(self, Quantum, Overload):
        self.Quantum = Quantum
        self.Overload = Overload

    def TurnAround(self, ProcessList):
        Turnaround = 0
        for process in ProcessList:
            Turnaround += process.WaitTime + process.ExecutionTime
        return Turnaround/ProcessList.size

    # Escalonamento
    def FIFO(self, ProcessArray):
        """This function implement the first in first out (FIFO) algorithm. 
        It's a no preemptive algorithm in which the CPU executes in order the process that arrive.

        Args:
            ProcessArray (Array): An array containing all the process in the instantiated.
        """
        CopyArray = np.array([]) 

        for process in ProcessArray: # copia pq python é so por referencia
            CopyArray = np.append(CopyArray, process.clone() )

        WorkingList = np.array(CopyArray) #List with process to be executed
        TotalTime = 0
        ProcessCount = CopyArray.size
        ExecutingProcess = None #Process in execution

        #execuçao dos processos
        while ProcessCount != 0:

            #Escolhe o proximo
            if ExecutingProcess == None: # so escolhe o proximo se nenhum estiver sendo executado
                for process in WorkingList:
                    if process.StartTime <= TotalTime: # escolhe o primeiro caso alguem ja tenho chegado
                        ExecutingProcess = process
                        break

            TotalTime += 1
            print("Tempo atual:" + str(TotalTime))

            try:
                ExecutingProcess.ExecutedTime += 1

                if ExecutingProcess.ExecutedTime == ExecutingProcess.ExecutionTime: # Remove o processo caso tenha terminado
                        WorkingList = np.delete(WorkingList, np.where(WorkingList == ExecutingProcess))
                        ExecutingProcess = None
                        ProcessCount -= 1
            except:
                pass

            #Tempo de espera para calculo de turnaround
            for process in WorkingList:
                if (process == ExecutingProcess) or (process.StartTime >= TotalTime):#não conta se é o que ta execuntado ou ainda "não chegou"
                    continue
                process.WaitTime += 1


            for process in CopyArray:
                process.print_process()        
            print("----------------------------")
        
        print("TotalTime : ")
        print(TotalTime)
        print("----------------------------------")
        

        print("Turnaround : ")
        print(self.TurnAround(CopyArray))
        print("----------------------------------")
        return


    def Sjf(self, ProcessArray):
        """This function implement the shortest job first algorithm
        It's a no preemptive algorithm in which the scheduler choses the process with the smallest execution time for the next execution.

        Args:
            ProcessArray (_type_): _description_
        """
        CopyArray = np.array([]) 

        for process in ProcessArray: # copia pq python é so por referencia
            CopyArray = np.append(CopyArray, process.clone() )

        WorkingList = np.array(CopyArray)
        TotalTime = 0
        ProcessCount = CopyArray.size
        ExecutingProcess = None

        #execuçao dos processos
        while ProcessCount != 0:
            #Escolhe o proximo
            if ExecutingProcess == None: # so escolhe o proximo se nenhum estiver sendo executado
                for process in WorkingList:
                    if process.StartTime <= TotalTime : # so escolhe o proximo caso alguem ja tenho chegado
                        if ExecutingProcess == None: # escolhe o 1 para comparação
                            ExecutingProcess = process
                        else: # encontra o com menor job dos que ja chegaram
                            if process.ExecutionTime - process.ExecutedTime  < ExecutingProcess.ExecutionTime - ExecutingProcess.ExecutedTime:
                                ExecutingProcess = process

            TotalTime += 1
            print("Tempo atual:" + str(TotalTime))

            try:
                ExecutingProcess.ExecutedTime += 1

                if ExecutingProcess.ExecutedTime == ExecutingProcess.ExecutionTime: # Remove o processo caso tenha terminado
                        WorkingList = np.delete(WorkingList, np.where(WorkingList == ExecutingProcess))
                        ExecutingProcess = None
                        ProcessCount -= 1
            except:
                pass
            #Tempo de espera para calculo de turnaround
            for process in WorkingList:
                if (process == ExecutingProcess) or (process.StartTime >= TotalTime):#não conta se é o que ta execuntado ou ainda "não chegou"
                    continue
                process.WaitTime += 1

                
            for process in CopyArray:
                process.print_process()        
            print("----------------------------")
        
        print("TotalTime : ")
        print(TotalTime)
        print("----------------------------------")
        print("Turnaround : ")
        print(self.TurnAround(CopyArray))
        print("----------------------------------")
        return


    def RoundRobin(self, ProcessArray):
        """This function implement the round robin algorithm
        It's a preemptive algorithm in which time slices (quanta) are assigned to each process in equal portions and circular order.

        Args:
            ProcessArray (_type_): _description_
        """
        WorkingArray = np.array([]) 

        for process in ProcessArray: # copia pq python é so por referencia
            WorkingArray = np.append(WorkingArray, process.clone() )

        CopyArray = np.array(WorkingArray)

        ReadyList = np.array([])
        TotalTime = 0
        ProcessCount = WorkingArray.size
        ExecutingProcess = None

        Overloading = False
        OverloadTime = self.Overload

        #execuçao dos processos
        while ProcessCount != 0:

            for process in WorkingArray: # so coloca na lista de prontos se já chegou
                if process.StartTime <= TotalTime:
                    ReadyList = np.append(ReadyList, process)
                    WorkingArray = np.delete(WorkingArray, np.where(WorkingArray == process))
            

            if ExecutingProcess == None: # escolhe o primeiro dos prontos se nenhum estiver sendo executado
                for process in ReadyList:
                    ExecutingProcess = process
                    break

            TotalTime += 1
            print("Tempo atual:" + str(TotalTime))

            # Executando
            if not Overloading:
                try:
                    ExecutingProcess.ExecutedTime += 1
                    ExecutingProcess.ExecutionTimePerQuantum += 1

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
                    process.WaitTime += 1

            else:
                print("Overloading")
                ReadyList = np.delete(ReadyList, np.where(ReadyList == ExecutingProcess))
                ReadyList = np.append(ReadyList, ExecutingProcess)

                
                for process in ReadyList:
                    if process.StartTime > TotalTime:#não sei se é necessario mas ta funcionando com
                        continue
                    process.WaitTime += 1
                OverloadTime -= 1
                if OverloadTime <= 0: # terminando overload
                    OverloadTime = self.Overload
                    ExecutingProcess = None
                    Overloading = False
              
            for process in CopyArray:
                process.print_process()        
            print("----------------------------")

        
        print("TotalTime : ")
        print(TotalTime)
        print("----------------------------------")
        

        print("Turnaround : ")
        print(self.TurnAround(CopyArray))
        print("----------------------------------")
        return

    def Edf(self, ProcessArray):
        """This function implement the earliest deadline first algorithm
        It's a dynamic priority algorithm in which there's a priority queue based on the closeness to each process' deadline.
        Args:
            ProcessArray (_type_): _description_
        """
        WorkingArray = np.array([]) 

        for process in ProcessArray: # copia pq python é so por referencia
            WorkingArray = np.append(WorkingArray, process.clone() )

        CopyArray = np.array(WorkingArray)

        ReadyList = np.array([])
        TotalTime = 0
        ProcessCount = WorkingArray.size
        ExecutingProcess = None

        Overloading = False
        OverloadTime = self.Overload

        #execuçao dos processos
        while ProcessCount != 0:

            for process in WorkingArray:# so coloca na lista de prontos se já chegou
                if process.StartTime <= TotalTime:
                    ReadyList = np.append(ReadyList, process)
                    WorkingArray = np.delete(WorkingArray, np.where(WorkingArray == process))
            



            if ExecutingProcess == None: # so escolhe o proximo se nenhum estiver sendo executado
                for process in ReadyList:
                    if process.StartTime <= TotalTime : # so escolhe o proximo caso alguem ja tenho chegado
                        if ExecutingProcess == None: # escolhe o 1 para comparação
                            ExecutingProcess = process
                        else: # encontra o deadline mais ceda dos que ja chegaram
                            if process.Deadline - (TotalTime - process.StartTime)  < ExecutingProcess.Deadline - (TotalTime - ExecutingProcess.StartTime):
                                ExecutingProcess = process

            TotalTime += 1
            print("Tempo atual:" + str(TotalTime))

            # Executando
            if not Overloading:
                try:
                    ExecutingProcess.ExecutedTime += 1
                    ExecutingProcess.ExecutionTimePerQuantum += 1

                    if ExecutingProcess.Deadline - (TotalTime - ExecutingProcess.StartTime) < 0:
                        ExecutingProcess.MetDeadline = False

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
                    process.WaitTime += 1
            else:
                print("Overloading")
                ReadyList = np.delete(ReadyList, np.where(ReadyList == ExecutingProcess))
                ReadyList = np.append(ReadyList, ExecutingProcess)

                
                for process in ReadyList:
                    if process.StartTime > TotalTime:#não sei se é necessario mas ta funcionando com
                        continue
                    process.WaitTime += 1
                OverloadTime -= 1
                if OverloadTime <= 0: # terminando overload
                    OverloadTime = self.Overload
                    ExecutingProcess = None
                    Overloading = False
                
              
            for process in CopyArray:
                process.print_process()        
            print("----------------------------")

        
        print("TotalTime : ")
        print(TotalTime)
        print("----------------------------------")
        

        print("Turnaround : ")
        print(self.TurnAround(CopyArray))
        print("----------------------------------")
        return


if __name__ == "__main__":

    # outros processos
    ProcessA = Process.process(0,4,7,0,0,1)
    ProcessB = Process.process(2,2,3,0,0,2)
    ProcessC = Process.process(4,1,5,0,0,3)
    ProcessD = Process.process(6,3,10,0,0,4)


    # processos da prova
    Process1 = Process.process(0,4,35,0,0,1)
    Process2 = Process.process(3,2,15,0,0,2)
    Process3 = Process.process(6,7,20,0,0,3)
    Process4 = Process.process(9,8,25,0,0,4)

    # outros processos
    ProcessArray = np.array([ProcessA,ProcessB,ProcessC,ProcessD,])

    # processos da prova
    ProcessArray1 = np.array([Process1,Process2,Process3,Process4,])

    scheduler = ProcessScheduler(2 , 1)

    #scheduler.FIFO(ProcessArray)
    #scheduler.Sjf(ProcessArray)

    #scheduler.RoundRobin(ProcessArray)

    #scheduler.Edf(ProcessArray)

    #scheduler.FIFO(ProcessArray1)
    #scheduler.Sjf(ProcessArray1)

    #scheduler.RoundRobin(ProcessArray1)

    scheduler.Edf(ProcessArray1)
