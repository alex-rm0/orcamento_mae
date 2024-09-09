import streamlit as st
import pandas as pd

def show():
    st.subheader("Histórico de Faturas")

    # Opções de mês e categoria
    meses = ["Todos os Meses", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    mes_selecionado = st.selectbox("Selecione o mês:", meses)

    categorias = [
        "Todas as Categorias",
        "Educação - Livros",
        "Educação - Propinas",
        "Alimentação - Restaurante",
        "Alimentação - Supermercado",
        "Casa - Empréstimos",
        "Casa - Empregadas",
        "Casa - Impostos",
        "Casa - Obras",
        "Casa - Água e Luz",
        "Casa - Condomínio",
        "Vestuário",
        "Saúde - Farmácia",
        "Saúde - Nutrição",
        "Saúde - Médico",
        "Veículos - Gasolina",
        "Veículos - Oficina",
        "Veículos - Impostos",
        "Veículos - Portagens",
        "Diversos - Outros"
    ]
    categoria_selecionada = st.selectbox("Selecione a categoria:", categorias)

    # Botão para exibir faturas
    if st.button("Exibir Faturas"):
        faturas_filtradas = []

        with open("faturas.txt", "r") as file:
            for line in file:
                parts = line.strip().split(", ")
                
                # Certifique-se de que há partes suficientes e que o formato é correto
                if len(parts) < 4:
                    continue  # Pula a linha se não tiver partes suficientes
                
                if len(parts[1]) < 10:
                    continue  # Pula a linha se a parte 'Categoria' não tiver caracteres suficientes
                
                try:
                    valor = float(parts[3][7:])  # Tenta converter o valor
                except ValueError:
                    st.warning(f"Valor inválido na linha: {line}")  # Exibe um aviso se o valor for inválido
                    continue
                
                data = {
                    "Mês": parts[0][6:],  
                    "Categoria": parts[1][10:],  
                    "Descrição": parts[2][11:], 
                    "Valor": valor  # Usa o valor convertido
                }
                
                if (mes_selecionado == "Todos os Meses" or mes_selecionado == data["Mês"]) and \
                   (categoria_selecionada == "Todas as Categorias" or categoria_selecionada == data["Categoria"]):
                    faturas_filtradas.append(data)

        # Converte os dados filtrados para um DataFrame
        if faturas_filtradas:
            df = pd.DataFrame(faturas_filtradas)
            st.dataframe(df)  # Exibe a tabela de faturas filtradas
        else:
            st.info("Não há faturas para o mês e categoria selecionados.")
