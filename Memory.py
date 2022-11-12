import numpy as np
import Pages
class Memory:
    def __init__(self):
        self.PageSize = 4 # tamanho da pagina
        self.Space = 200 # tamanho total da memoria
        Page= []  
        for i in range(50):
            Page.append(Pages.Page(None))
        self.PageList = np.array(Page) # Array com cada pagina                   
        self.EmptyPagesNum = 50

    def clone(self):
        Mem = Memory()
        Mem.PageSize = self.PageSize
        Mem.Space = self.Space
        Mem.PageList = self.PageList
        return Mem

    def FindOldest(self): # retorna o processo mais antigo

        Oldest = self.PageList[0]

        for page in self.PageList:
            if page.Process == None: # assumindo que nunca vai ter um buraco no meio da lista
                break
            if page.RecentlyUsed < Oldest.RecentlyUsed:
                Oldest = page

        return Oldest.Process

    def RemoveProcess(self,Process, VMem):

        for index, page in np.ndenumerate(self.PageList): # itera sobre as paginas na memoria 
            if page.Process == Process: # se encontrar o processo 
                VMem.PageList[page.VirtualMemoryAddress].RamAdress = -1 # tira a referencia na memoria vi
                page.VirtualMemoryAddress = -1
                page.Process = None
                LastIndex = index[0]

        self.EmptyPagesNum += Process.MemoryPages
        self.Defrag(LastIndex + 1, Process.MemoryPages, VMem)
        return

    def Defrag(self, LastIndex, AmmountRemoved, VMem):
        print("Last index " + str(LastIndex))
        print("AmmountRemoved " + str(AmmountRemoved))
        for i in range(LastIndex , 50):
            VMemAdress = self.PageList[i].VirtualMemoryAddress

            # copia do processo para a posiçao do que foi removido
            self.PageList[i-AmmountRemoved].Process = self.PageList[i].Process
            self.PageList[i-AmmountRemoved].VirtualMemoryAddress = self.PageList[i].VirtualMemoryAddress
            self.PageList[i-AmmountRemoved].RecentlyUsed = self.PageList[i].RecentlyUsed

            #atualização na virtual
            VMem.PageList[VMemAdress].RamAdress = i - AmmountRemoved
            
            # Remoção do princiapl
            self.PageList[i].Process = None
            self.PageList[i].VirtualMemoryAddress = -1

        return
    
    def Update(self):
        for page in self.PageList:
            if page.Process == None: # assumindo que não tem um burcao no meio da memoria
                break
            page.RecentlyUsed -= 1
        return