import numpy as np
import Process
import Pages
import Memory
import VirtualMemory

from interface import *

class MemoryScheduler:
    def __init__ (self):
        pass

    #Escalonamento
    def FIFO(self,Mem, VMem, Process):
        IndexProcessPages = VMem.FindProcess(Process)

        if VMem.PageList[IndexProcessPages[0]].RamAdress != -1: # processo ja esta na memoria
            return
        
        # por padrão o procceso que chegou primeiro é colocado no começo, já que é o fifo
        # e os ultimos vao ser colocados no final  
        
        # a memoria ta cheia e o processo não ta nela
        while Mem.EmptyPagesNum < Process.MemoryPages:
            
            Mem.RemoveProcess(Mem.PageList[0].Process,VMem)

        # a memoria tem espaço vazio ou estava cheia mas um processo ja foi removido
        for i in range(50):
            if Mem.PageList[i].Process == None: # quando encontrar o primeiro espaço vazio
                j = 0
                for page in IndexProcessPages: # liga as paginas na memoria virtual e na real e coloca o processo na real
                    VMem.PageList[page].RamAdress = i+j
                    Mem.PageList[i+j].Process = Process
                    Mem.PageList[i+j].RecentlyUsed = 50
                    Mem.PageList[i+j].VirtualMemoryAddress = page
                    j += 1   
                Mem.EmptyPagesNum -= Process.MemoryPages
                return  

        return

    def LRU(self,Mem, VMem, Process):
        IndexProcessPages = VMem.FindProcess(Process)

        if VMem.PageList[IndexProcessPages[0]].RamAdress != -1: # processo ja esta na memoria
            for index in IndexProcessPages:
                Adress = VMem.PageList[index].RamAdress
                Mem.PageList[Adress].RecentlyUsed = 50
            Mem.Update() # atualiza a ultima vez que cada processo foi utilizado
            return
            
        # a memoria ta cheia e o processo não ta nela
        while Mem.EmptyPagesNum < Process.MemoryPages:
            a = Mem.FindOldest()
            Mem.RemoveProcess(a, VMem)


        # a memoria tem espaço vazio ou estava cheia mas um processo já foi removido
        for i in range(50):
            if Mem.PageList[i].Process == None: # quando encontrar o primeiro espaço vazio
                j = 0
                for page in IndexProcessPages: # liga as paginas na memoria virtual e na real e coloca o processo na real
                    VMem.PageList[page].RamAdress = i+j
                    Mem.PageList[i+j].Process = Process
                    Mem.PageList[i+j].RecentlyUsed = 50
                    Mem.PageList[i+j].VirtualMemoryAddress = page
                    j += 1   
                Mem.EmptyPagesNum -= Process.MemoryPages
                Mem.Update() # atualiza a ultima vez que cada processo foi utilizado
                return  
        Mem.Update() # atualiza a ultima vez que cada processo foi utilizado
        return


if __name__ == "__main__":

    ProcessA = Process.process(0,4,7,0,17,1)
    ProcessB = Process.process(2,2,3,0,17,2)
    ProcessC = Process.process(4,1,5,0,17,3)
    ProcessD = Process.process(6,3,10,0,17,4)


    ProcessArray = np.array([ProcessA,ProcessB,ProcessC,ProcessD,])

    scheduler = MemoryScheduler()
    Mem = Memory.Memory()
    VMem = VirtualMemory.VirtualMemory(ProcessArray)

    """ scheduler.FIFO(Mem, VMem, ProcessA)
    scheduler.FIFO(Mem, VMem, ProcessB)
    scheduler.FIFO(Mem, VMem, ProcessA)
    scheduler.FIFO(Mem, VMem, ProcessD)
    scheduler.FIFO(Mem, VMem, ProcessC) """

    scheduler.LRU(Mem, VMem, ProcessA)
    scheduler.LRU(Mem, VMem, ProcessB)
    scheduler.LRU(Mem, VMem, ProcessA)
    scheduler.LRU(Mem, VMem, ProcessD)
    scheduler.LRU(Mem, VMem, ProcessC)

    print("a")
    print("a")
    print("a")
