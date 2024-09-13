import streamlit as st
from datetime import datetime
import pandas as pd

# Inicializa o st.session_state para armazenar faturas, se ainda não estiver definido
if 'faturas' not in st.session_state:
    st.session_state.faturas = []

def insert():
    st.subheader("Inserir Fatura")

    # Seleção do mês e categorias
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    mes = st.selectbox("Selecione o mês:", meses, index=datetime.now().month - 1)

    categorias = [
        "Educação - Livros", "Educação - Propinas", "Alimentação - Restaurante", "Alimentação - Supermercado",
        "Casa - Empréstimos", "Casa - Empregadas", "Casa - Impostos", "Casa - Obras", "Casa - Água e Luz",
        "Casa - Condomínio", "Vestuário", "Saúde - Farmácia", "Saúde - Nutrição", "Saúde - Médico",
        "Veículos - Gasolina", "Veículos - Oficina", "Veículos - Impostos", "Veículos - Portagens", "Diversos - Outros"
    ]
    categoria = st.selectbox("Selecione a categoria:", categorias)

    # Campos de entrada
    descricao = st.text_input("Descrição:")
    valor = st.text_input("Valor:")

    # Botão para adicionar a fatura
    if st.button("Adicionar Fatura"):
        if descricao and valor:
            # Verifica se o valor contém vírgula e impede a adição
            if "," in valor:
                st.error("Use ponto (.) em vez de vírgula (,)")
            else:
                try:
                    # Tenta converter o valor para float para garantir que é numérico
                    valor_float = float(valor)
                    
                    # Adiciona a fatura no st.session_state
                    st.session_state.faturas.append({
                        "Data": mes,
                        "Categoria": categoria,
                        "Descrição": descricao,
                        "Valor": valor_float
                    })
                    st.success("Fatura adicionada com sucesso!")
                except ValueError:
                    st.error("Por favor, insira um valor numérico válido.")
        else:
            st.error("Por favor, preencha todos os campos.")

    st.subheader("Remover Fatura")
    
    # Cria um DataFrame das faturas no session_state
    if st.session_state.faturas:
        df = pd.DataFrame(st.session_state.faturas)
        
        # Exibe a tabela
        st.write("Tabela de Faturas")
        st.dataframe(df)

        # Permite selecionar as faturas para remover
        st.write("Selecione as faturas a remover:")
        selected_indices = st.multiselect(
            "Faturas para remover:",
            options=df.index,
            format_func=lambda i: f"{df.iloc[i]['Data']} - {df.iloc[i]['Categoria']} - {df.iloc[i]['Descrição']} - {df.iloc[i]['Valor']}"
        )

        # Botão para remover faturas selecionadas
        if st.button("Remover Faturas Selecionadas"):
            # Remove as faturas selecionadas do session_state
            st.session_state.faturas = [f for i, f in enumerate(st.session_state.faturas) if i not in selected_indices]
            st.success("Faturas selecionadas foram removidas.")
    else:
        st.info("Não há faturas para remover.")
