class process:
    def __init__(self, StartTime = 0, ExecutionTime = 0, Deadline = 0, Priority = 0, MemoryPages = 0, ProcessId = 0 )
        self.StartTime = StartTime
        self.ExecutionTime = ExecutionTime
        self.ExecutedTime = 0
        self.ExecutionTimePerQuantum = 0
        self.WaitTime = 0
        self.Deadline = Deadline
        self.Priority = Priority
        self.ProcessId = ProcessId
        self.MemoryPages = MemoryPages
        self.MemorySize = 4 # mudar para 4098 ?
        self.MetDeadline = True

    def clone(self):
        proc = process()
        proc.ProcessId = self.ProcessId
        proc.StartTime = self.StartTime
        proc.ExecutionTime = self.ExecutionTime
        proc.ExecutedTime = self.ExecutedTime
        proc.ExecutionTimePerQuantum = self.ExecutionTimePerQuantum
        proc.WaitTime = self.WaitTime
        proc.Deadline = self.Deadline
        proc.Priority = self.Priority
        proc.MemoryPages = self.MemoryPages
        proc.MemorySize = self.MemorySize
        proc.MetDeadline = self.MetDeadline
        return proc

    def print_process(): #Inacabado (Rodrigo)
        print(f"Chegada: {str(self.StartTime)}")
        print(f"Job: {str(self.ExecutionTime)}")
        print(f"Tempo executado: {str(self.ExecutedTime)}")
        print(f"Tempo de Espera: {str(self.WaitTime)}")
        print(f"ProcessCount: {str(self.ProcessCount)}")        
        return
