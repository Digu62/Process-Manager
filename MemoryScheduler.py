import numpy as np
import Process
import Pages
import Memory
import VirtualMemory

class MemoryScheduler:
    def __init__ (self):
        pass

    #Escalonamento
    def FIFO(self,Mem, VMen, Process):
        
        IndexProcessPages = VMen.FindProcess(Process)

        if VMen.PageList[IndexProcessPages[0]].RamAdress != -1: # processo ja esta na memoria
            return
            
        # a memoria ta cheia e o processo não ta nela
        while Mem.EmptyPagesNum < Process.MemoryPages:

            # por padrão estou colocando o que chegou primeiro no começo, já que é o fifo
            # e os ultimos vao ser colocados no fim

        
            Mem.RemoveProcess(Mem.PageList[0].Process)

            # --------------------------------------------------------------------------------------------------------------------------#
            # Falta adcionar swap                                                                                                       #
            # RemoveProcess nao guarda no disco                                                                                         #
            # Não acho que é necessario guardar no disco, pois todas as informações que a gente precisa tão guardados no processo em si #
            # - Fernando    
            # mas ai que ta, a abstração do disco ta na propia classe do processo + a lista de processos que a gente passsa             # 
            #---------------------------------------------------------------------------------------------------------------------------#

        # a memoria tem espaço vazio
        for i in range(50):
            if Mem.PageList[i].Process == None: # quando encontrar o primeiro espaço vazio
                j = 0
                for page in IndexProcessPages: # liga as paginas na memoria virtual e na real e coloca o processo na real
                    VMen.PageList[page].RamAdress = i+j
                    Mem.PageList[i+j].Process = Process
                    Mem.PageList[i+j].RecentlyUsed = 50
                    Mem.PageList[i+j].VirtualMemoryAddress = page
                    j += 1   
                Mem.EmptyPagesNum -= Process.MemoryPages
            return  

        return

    def LRU(self,Mem, VMen, Process):
        IndexProcessPages = VMen.FindProcess(Process)

        if VMen.PageList[IndexProcessPages[0]].RamAdress != -1: # processo ja esta na memoria
            for index in IndexProcessPages:
                Adress = VMen.PageList[index].RamAdress
                Mem.PageList[Adress].RecentlyUsed = 50
            Mem.Update()
            return
            
        # a memoria ta cheia e o processo não ta nela
        while Mem.EmptyPagesNum < Process.MemoryPages:

            # por padrão estou colocando o que chegou primeiro no começo, já que é o fifo
            # e os ultimos vao ser colocados no fim

        
            Mem.RemoveProcess(Mem.FindOldest())

            # --------------------------------------------------------------------------------------------------------------------------#
            # Falta adcionar swap                                                                                                       #
            # RemoveProcess nao guarda no disco                                                                                         #
            # Não acho que é necessario guardar no disco, pois todas as informações que a gente precisa tão guardados no processo em si #
            # - Fernando    
            # mas ai que ta, a abstração do disco ta na propia classe do processo + a lista de processos que a gente passsa             # 
            #---------------------------------------------------------------------------------------------------------------------------#

        # a memoria tem espaço vazio
        for i in range(50):
            if Mem.PageList[i].Process == None: # quando encontrar o primeiro espaço vazio
                j = 0
                for page in IndexProcessPages: # liga as paginas na memoria virtual e na real e coloca o processo na real
                    VMen.PageList[page].RamAdress = i+j
                    Mem.PageList[i+j].Process = Process
                    Mem.PageList[i+j].RecentlyUsed = 50
                    Mem.PageList[i+j].VirtualMemoryAddress = page
                    j += 1   
                Mem.EmptyPagesNum -= Process.MemoryPages
            Mem.Update()
            return  
        Mem.Update()
        return


if __name__ == "__main__":

    ProcessA = Process.process(0,4,7,0,5,1)
    ProcessB = Process.process(2,2,3,0,5,2)
    ProcessC = Process.process(4,1,5,0,5,3)
    ProcessD = Process.process(6,3,10,0,5,4)


    ProcessArray = np.array([ProcessA,ProcessB,ProcessC,ProcessD,])

    scheduler = MemoryScheduler()
    Mem = Memory.Memory()
    VMem = VirtualMemory.VirtualMemory(ProcessArray)

    scheduler.FIFO(Mem, VMem, ProcessB)

    print("a")
    print("a")
    print("a")