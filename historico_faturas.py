import streamlit as st
import pandas as pd

# Função para exibir o histórico de faturas
def show():
    st.subheader("Histórico de Faturas")

    # Verifica se o session_state já contém faturas
    if 'faturas' not in st.session_state:
        st.session_state.faturas = []

    # Opções de filtro por mês e categoria
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

        # Filtra as faturas no session_state
        for fatura in st.session_state.faturas:
            mes_fatura = fatura["Data"]
            categoria_fatura = fatura["Categoria"]

            if (mes_selecionado == "Todos os Meses" or mes_selecionado == mes_fatura) and \
               (categoria_selecionada == "Todas as Categorias" or categoria_selecionada == categoria_fatura):
                faturas_filtradas.append(fatura)

        # Converte os dados filtrados para um DataFrame
        if faturas_filtradas:
            df = pd.DataFrame(faturas_filtradas)
            st.dataframe(df)  # Exibe a tabela de faturas filtradas
        else:
            st.info("Não há faturas para o mês e categoria selecionados.")
