class Page:
    def __init__(self, Process, RecentlyUsed = 50):
        self.Process = Process # processo armazenado na pagina
        self.RecentlyUsed = RecentlyUsed # contador para ultima vez que foi utilizado
        self.VirtualMemoryAddress = -1 # referencia a memoria virtual

class VirtualPage:
    def __init__(self, Process):
        self.Process = Process
        self.RamAdress = -1 
