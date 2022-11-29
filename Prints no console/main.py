from ProcessScheduler import *
from Process import *
import numpy as np


ProcessNumber = int( input("Número de processos") )

ProcessArray = np.array([])

for i in range(ProcessNumber):
    ProcessStart = int(input("Tempo de chegada do processo " + i))
    ProcessExecution = int(input("Tempo de execução do processo " + i))
    ProcessDeadline = int(input("Deadline do processo " + i))
    ProcessPriority = int(input("Prioridade do processo " + i))
    ProcessPage = int(input("Páginas na memória do processo " + i))
    Proc = process(ProcessStart,ProcessExecution,ProcessDeadline,ProcessPriority,ProcessPage,i)
    ProcessArray = np.append(ProcessArray,Proc)

Quantum = int(input("Quantum do sistema: "))
Overload = int(input("Overload do sistema: "))

ProcAlgo = int(input("Escalonamento de processos : 1-FIFO  2-SJF  3-RoundRobin  4-EDF"))
MemAlgo = int(input("Escalonamento de Memoria : 1-FIFO  2-LRU"))

scheduler = ProcessScheduler(Quantum,Overload)

if ProcAlgo == 1:
    scheduler.FIFO(ProcessArray,MemAlgo)
elif ProcAlgo == 2:
    scheduler.Sjf(ProcessArray,MemAlgo)
elif ProcAlgo == 3:
    scheduler.RoundRobin(ProcessArray,MemAlgo)
elif ProcAlgo == 4:
    scheduler.Edf(ProcessArray,MemAlgo)
