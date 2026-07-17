import random
import pandas as pd
import streamlit as st

from configurations.config import logger

st.set_page_config(
    page_title="Escalonador",
    page_icon="assets/icon.ico",
    layout="wide",
)

if "tela" not in st.session_state:
    st.session_state.tela = "main"

if "actual_process" not in st.session_state:
        st.session_state.actual_process = 1

if "process_list" not in st.session_state:
    st.session_state.process_list = pd.DataFrame(columns=[
        "id", "start_process", "execution_time", "deadline", "priority", "pages_in_memory"
    ])

def start():
    col = st.columns(3)

    #Cria o conteudo no centro da tela
    with col[1]:
        st.subheader("Escalonador de Processos")

        num_processes = st.number_input("Número de processos", min_value=1, max_value=10)
        quantum = st.number_input("Quantum do sistema", min_value=1, max_value=10)
        overload = st.number_input("Sobreacarga do sistema", min_value=1, max_value=10)

        #Botão acionado apos preenchimento d todos os campos
        if st.button("Proximo"):
            # Verificar se os campos foram preenchidos corretamente
            st.session_state.num_processes = num_processes
            st.session_state.quantum = quantum
            st.session_state.overload = overload
            st.session_state.tela = "log"
            st.rerun()

def log():

    col = st.columns([1,2,1])
    
    #Preenche os processos com valores vazios
    if st.session_state.process_list.empty:
        for process in range(st.session_state.num_processes):
            st.session_state.process_list.loc[len(st.session_state.process_list)] ={
                "id": process+1,
                "start_process": None,
                "execution_time": None,
                "deadline": None,
                "priority": None,
                "pages_in_memory": None
            }

    #Exibi os dados dos processos
    with col[0]:
        st.write("Dados dos processos")
        st.dataframe(st.session_state.process_list.T)
        

    #Exibe a seção de preenchimento dos processos
    with col[1]:
        top_cols = st.columns(3)
        with top_cols[0]:
            if st.button("Voltar"):
                st.session_state.tela = "main"
                st.session_state.count_process = 1
                if "process_list" in st.session_state:
                    del st.session_state.process_list 
                st.session_state.num_processes = None
                st.rerun()
                
        # with top_cols[1]:
        st.markdown(
            f"""
            <h2 style='font-size:28px; text-align:center;'>
                Processo Atual: {st.session_state.actual_process}
            </h2>
            """,
            unsafe_allow_html=True
        )
        st.markdown("---")  # Linha divisória opcional
        st.empty()

        #Randomiza os valores dos processos
        with top_cols[2]:
            if st.button("Randomizar Processo"):
                #TODO Implementar logica de restrição para que os processos randomicos sejam coerentes e aplicaveis
                st.session_state.start = random.randint(0, 10)
                st.session_state.exec = random.randint(1, 10)
                st.session_state.dead = random.randint(1, 10)
                st.session_state.prior = random.randint(1, 10)
                st.session_state.pages = random.randint(1, 10)
                st.rerun()

        #Recebe os dados dos processos
        st.text(f"Processo {st.session_state.actual_process}")
        start_process = st.number_input("Inicio do processo", min_value=0, key="start")
        execution_time = st.number_input("Tempo de execução", min_value=1, key="exec")
        deadline = st.number_input("Deadline", min_value=1, key="dead")
        priority = st.number_input("Prioridade", min_value=1, key="prior")
        pages_in_memory = st.number_input("Páginas na memória", min_value=1, key="pages")

        #Define os valores dos processos
        bottom_cols = st.columns(2)
        with bottom_cols[0]:
            if st.button("Definir Processo"):
                logger.debug(f"st.session_state.count_process:{st.session_state.actual_process}")
                logger.debug(f"st.session_state.num_processes:{st.session_state.num_processes}")
                if st.session_state.actual_process <= st.session_state.num_processes:
                    #Atualiza os dados do processo selecionado
                    st.session_state.process_list.loc[st.session_state.actual_process - 1, "start_process"] = start_process
                    st.session_state.process_list.loc[st.session_state.actual_process - 1, "execution_time"] = execution_time
                    st.session_state.process_list.loc[st.session_state.actual_process - 1, "deadline"] = deadline
                    st.session_state.process_list.loc[st.session_state.actual_process - 1, "priority"] = priority
                    st.session_state.process_list.loc[st.session_state.actual_process - 1, "pages_in_memory"] = pages_in_memory
                    if st.session_state.actual_process != st.session_state.num_processes:#TODO Otimizar
                        st.session_state.actual_process += 1
                    st.rerun()
                # else:
                #     st.success("Todos os processos foram adicionados!")
                #     st.rerun()
                #     # Aqui você pode adicionar a lógica para processar os dados coletados
                
        with bottom_cols[1]:
            if st.button("Finalizar"):
                #TODO Validar preenchimento de todos os processos
                st.session_state.tela = "scaler"
                st.rerun()
    
    #Exibe a seção de seleção dos processos
    with col[2]:
        # # Inicializa o índice selecionado
        # if "selected_process_idx" not in st.session_state:
        #     st.session_state.selected_process_idx = 0

        st.write("Processos preenchidos")
        n_process = st.session_state.get("num_processes", 0)
        max_per_row = 3
        rows = (n_process + max_per_row - 1) // max_per_row


        for row in range(rows):
            cols = st.columns(min(max_per_row, n_process - row * max_per_row))
            for i in range(min(max_per_row, n_process - row * max_per_row)):
                idx = row * max_per_row + i + 1
                if idx == st.session_state.actual_process:
                    # Botão selecionado: destaque visual
                    cols[i].markdown(
                        f"""
                        <div style='
                            background-color:#569BAA;
                            color:white;
                            border-radius:8px;
                            padding:8px 0;
                            text-align:center;
                            font-weight:bold;
                            border:2px solid #2d6a7a;
                            margin-bottom:4px;
                            display: flex;
                            justify-content: center;
                            align-items: center;
                            width: 100%;
                            max-width: 100px; /* ajuste conforme necessário */
                            margin-left: auto;
                            margin-right: auto;
                        '>
                            P{idx}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                else:
                    if cols[i].button(f"P{idx}"):
                        st.session_state.actual_process = idx
                        st.rerun()
                    cols[i].markdown("<div style='height:38px'></div>", unsafe_allow_html=True)

def scaler():
    process_scalers = ["FIFO", "SJF", "Round Robin", "EDF"]
    memory_scalers = ["Ordem de chegada", "MRU", "LRU"]

    cols = st.columns([1,3])
    with cols[0]:
        st.sidebar.title("🧠 Algoritmos de Escalonamento")

        st.sidebar.markdown("### ⚙️ Não Preemptivos")
        st.sidebar.markdown("- **FCFS (First-Come, First-Served)**: Executa na ordem de chegada. Simples, mas pode causar espera longa.")
        st.sidebar.markdown("- **SJF (Shortest Job First)**: Prioriza processos curtos. Eficiente, mas pode deixar processos longos esperando.")

        st.sidebar.markdown("### ⚡ Preemptivos")
        st.sidebar.markdown("- **Round Robin (RR)**: Cada processo recebe um tempo fixo (quantum). Ideal para sistemas interativos.")
        st.sidebar.markdown("- **Prioridade**: Executa processos com maior prioridade. Pode causar inanição dos de baixa prioridade.")
        st.sidebar.markdown("- **Multinível com Feedback**: Ajusta dinamicamente a prioridade com base no comportamento. Complexo, mas adaptável.")

        st.sidebar.markdown(
            """
            ### 📊 Métricas de Desempenho

            Algumas métricas são utilizadas para avaliar e comparar o desempenho dos algoritmos. São elas:

            - **🚀 Taxa de saída (Throughput)**  
            Quantidade de jobs concluídos por segundo.  
            *Valores elevados não indicam necessariamente bom desempenho.*

            - **⏱️ Tempo de retorno (Turnaround)**  
            Tempo médio para conclusão de um job a partir da sua submissão.

            - **🖥️ Uso de CPU**  
            Avalia se a CPU está sendo bem aproveitada ou se fica ociosa.
            """
        )

    with cols[1]:
        if st.button("Voltar", on_click=lambda: setattr(st.session_state, 'tela', 'log')):
            st.session_state.tela = "log"
            st.rerun()

        process_scaler = st.selectbox("Escolha o algoritmo:", process_scalers)
        memory_scaler = st.selectbox("Escolha o algoritmo:", memory_scalers)

        # import pandas as pd #TODO Usar para exportar e importar processos
        # st.title("📤 Upload de Arquivo CSV")
        # arquivo = st.file_uploader("Escolha um arquivo CSV", type="csv")
        # if arquivo is not None:
        #     df = pd.read_csv(arquivo)
        #     st.success("✅ Arquivo carregado com sucesso!")
        #     st.write("📊 Visualização dos dados:")
        #     st.dataframe(df)

        # if st.button("Executar simulação"): #TODO Usar para notificar inicio da simulação dos processos
        #     st.toast("🚀 Simulação iniciada!")

        # import time
        # with st.spinner("⏳ Processando dados..."): #TODO Usar para informar carregamentos
        #     time.sleep(2)
        # st.success("✅ Dados processados com sucesso!")

        if st.button("Continuar"):
            if memory_scaler and process_scaler:
                st.session_state.memory_scaler = memory_scaler
                st.session_state.process_scaler = process_scaler
                st.session_state.tela = "process"
            else:
                st.error("Por favor, selecione ambos os escalonadores antes de salvar.")
                return


def process():
    st.write("Processando...")


def update_screen():
    if st.session_state.tela == "main":
        start()
    elif st.session_state.tela == "log":
        log()
    elif st.session_state.tela == "scaler":
        scaler()
    elif st.session_state.tela == "process":
        process()

update_screen()
#Criar siste de preenchimento randomico

    