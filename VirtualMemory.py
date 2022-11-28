import numpy as np
import Pages
class VirtualMemory:
    def __init__(self, ProcessList):
        self.PageSize = 4 # tamanho da pagina

        # Cria as paginas na memoria virtual com o id do processo
        Page= []  
        for Process in ProcessList:
            for i in range(Process.MemoryPages):    
                Page.append(Pages.VirtualPage(Process))

        self.Space = len(Page)*4 # tamanho total da memoria
        self.PageList = np.array(Page) # Array com cada pagina
        


    def clone(self):
        Mem = VirtualMemory(None)
        Mem.PageSize = self.PageSize
        Mem.Space = self.Space
        Mem.PageList = self.PageList
        return Mem

    def ShowMemory(self):
        print("Memoria Virtual: Numero da pagina[Id do processo, Endereço da pagina na Ram]" )
        for i in range(self.PageList.size):
            print(f"{i}[{str(self.PageList[i].Process.ProcessId)},{str(self.PageList[i].RamAdress)}]",end=" ")
        print()
        print()
        return


    def FindProcess(self, process): # encontra indice das paginas virtuais do processo

        IndexList = []

        for index, page in np.ndenumerate(self.PageList):
            
            if page.Process == process:
                IndexList.append(index[0])


        return np.array(IndexList)