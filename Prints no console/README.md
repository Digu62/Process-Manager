Considere um sistemas operacional que implementa escalonamento de processos. O
funcionamento esperado é que esse ambiente tenha N processos que podem chegar em
tempos distintos para execução. Para cada processo, deve ser informado manualmente:
    o Tempo de chegada
    o Tempo de execução
    o Deadline
    o Prioridade
    o Quantum do sistema
    o Sobrecarga do sistema
● Esse sistema deve implementar os algoritmos de escalonamento:
    o FIFO
    o SJF
    o Round Robin
    o EDF
● Esse sistema deve implementar os algoritmos de substituição de páginas:
    o FIFO
    o Menos Recentemente Utilizado(LRU)
Requisitos:
    ● Cada processo deve ter até 10 páginas (entrada do usuário). Cada página tem 4K de
    tamanho. A RAM tem 200 K de memória.
    ● Crie a abstração de DISCO para utilização da memória virtual. Caso ocorra falta de
    página, utilize N u.t. para o uso do Disco.
        o O grupo está livre para a criação de qualquer abstração extra que se mostrar
        necessária.
        o Deve-se criar o gráfico de uso da RAM e do Disco, mostrando as páginas
        presentes em tempo-real.
    ● Os processos só executam se todas as suas páginas estiverem na RAM.
    ● Deve-se criar o gráfico de Gantt para mostrar as execuções dos processos, visualização
    da CPU e da RAM
    ● A resposta deve ser dada em função do turnaround médio (tempo de espera + tempo
    de execução)
    ● Colocar delay para verificar a execução
    - A linguagem de programação é de escolha do grupo.

    - simulador exemplo : https://lotusoregano.itch.io/operational-system-escalonator