import streamlit as st
from datetime import datetime

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
