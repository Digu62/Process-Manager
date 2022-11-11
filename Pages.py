class Page:
    def __init__(self, Process, RecentlyUsed = 50):
        self.Process = Process
        self.RecentlyUsed = RecentlyUsed
        self.VirtualMemoryAddress = -1

class VirtualPage:
    def __init__(self, Process):
        self.Process = Process
        self.RamAdress = -1 