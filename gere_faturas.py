import streamlit as st
from datetime import datetime
import pandas as pd

def insert():
    st.subheader("Inserir Fatura")

    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    mes = st.selectbox("Selecione o mês:", meses, index=datetime.now().month - 1)

    categorias = [
        "Educação - Livros", "Educação - Propinas", "Alimentação - Restaurante", "Alimentação - Supermercado",
        "Casa - Empréstimos", "Casa - Empregadas", "Casa - Impostos", "Casa - Obras", "Casa - Água e Luz",
        "Casa - Condomínio", "Vestuário", "Saúde - Farmácia", "Saúde - Nutrição", "Saúde - Médico",
        "Veículos - Gasolina", "Veículos - Oficina", "Veículos - Impostos", "Veículos - Portagens", "Diversos - Outros"
    ]
    categoria = st.selectbox("Selecione a categoria:", categorias)

    descricao = st.text_input("Descrição:")
    valor = st.text_input("Valor:")

    if st.button("Adicionar Fatura"):
        if descricao and valor:
            with open("faturas.txt", "a") as file:
                file.write(f"Data: {mes}, Categoria: {categoria}, Descrição: {descricao}, Valor: {valor}\n")
            st.success("Fatura adicionada com sucesso!")
        else:
            st.error("Por favor, preencha todos os campos.")

    st.subheader("Remover Fatura")
    
    # Lê e processa o arquivo de faturas
    faturas_remover = []
    with open("faturas.txt", "r") as file:
        for line in file:
            parts = line.strip().split(", ")
            data = {
                "Linha": line.strip(),  # Armazena a linha completa para facilitar a remoção
                "Data": parts[0][6:], 
                "Categoria": parts[1][10:],  
                "Descrição": parts[2][11:], 
                "Valor": float(parts[3][7:])  
            }
            faturas_remover.append(data)

    df = pd.DataFrame(faturas_remover)

    if not df.empty:
        # Adiciona uma coluna de checkbox
        df["Selecionar"] = df.index.to_series().apply(lambda i: st.checkbox("", key=f"checkbox_{i}"))

        # Exibe a tabela
        st.dataframe(df[["Data", "Categoria", "Descrição", "Valor", "Selecionar"]])

        # Botão para remover faturas selecionadas
        if st.button("Remover Faturas Selecionadas"):
            linhas_a_manter = df[~df["Selecionar"]]["Linha"].tolist()
            with open("faturas.txt", "w") as file:
                for linha in linhas_a_manter:
                    file.write(linha + "\n")
            st.success("Faturas selecionadas foram removidas.")
    else:
        st.info("Não há faturas para remover.")
