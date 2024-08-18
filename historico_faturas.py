import streamlit as st

def show():
    st.subheader("Histórico de Faturas")

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

    if st.button("Exibir Faturas"):
        st.write("Faturas para o mês e categoria selecionados:")
        with open("faturas.txt", "r") as file:
            for line in file:
                if (mes_selecionado == "Todos os Meses" or mes_selecionado in line) and \
                   (categoria_selecionada == "Todas as Categorias" or categoria_selecionada in line):
                    st.write(line.strip())
