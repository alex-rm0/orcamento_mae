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
            # Verifica se o valor contém uma vírgula e impede a adição
            if "," in valor:
                st.error("Usar ponto (.) em vez da vírgula (,)")
            else:
                try:
                    # Tenta converter o valor para float para garantir que é numérico
                    valor_float = float(valor)
                    
                    # Adiciona a fatura ao arquivo
                    with open("faturas.txt", "a") as file:
                        file.write(f"Data: {mes}, Categoria: {categoria}, Descrição: {descricao}, Valor: {valor_float}\n")
                    st.success("Fatura adicionada com sucesso!")
                except ValueError:
                    st.error("Por favor, insira um valor numérico válido.")
        else:
            st.error("Por favor, preencha todos os campos.")

    st.subheader("Remover Fatura")
    
    # Lê e processa o arquivo de faturas
    faturas_remover = []
    with open("faturas.txt", "r") as file:
        for line in file:
            parts = line.strip().split(", ")
            
            # Verificações de segurança para evitar erros de índice ou corte de string
            if len(parts) < 4:
                continue  # Pula a linha se não tiver partes suficientes
            
            if len(parts[0]) < 6 or len(parts[1]) < 10 or len(parts[2]) < 11 or len(parts[3]) < 7:
                continue  # Pula a linha se qualquer parte não tiver o comprimento mínimo esperado
            
            try:
                data = {
                    "Linha": line.strip(),  # Armazena a linha completa para facilitar a remoção
                    "Data": parts[0][6:], 
                    "Categoria": parts[1][10:],  
                    "Descrição": parts[2][11:], 
                    "Valor": float(parts[3][7:])
                }
                faturas_remover.append(data)
            except ValueError:
                continue  # Ignora a linha se ocorrer um erro de conversão de tipo

    df = pd.DataFrame(faturas_remover)

    if not df.empty:
        # Exibe a tabela
        st.write("Tabela de Faturas")
        st.dataframe(df[["Data", "Categoria", "Descrição", "Valor"]])

        st.write("Selecione as faturas a remover:")
        selected_indices = st.multiselect(
            "Faturas para remover:",
            options=df.index,
            format_func=lambda i: f"{df.iloc[i]['Data']} - {df.iloc[i]['Categoria']} - {df.iloc[i]['Descrição']} - {df.iloc[i]['Valor']}"
        )

        if st.button("Remover Faturas Selecionadas"):
            # Remove as faturas selecionadas
            linhas_a_manter = df.drop(selected_indices)["Linha"].tolist()
            with open("faturas.txt", "w") as file:
                for linha in linhas_a_manter:
                    file.write(linha + "\n")
            st.success("Faturas selecionadas foram removidas.")
    else:
        st.info("Não há faturas para remover.")
