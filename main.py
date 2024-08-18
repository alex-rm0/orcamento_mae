import streamlit as st
import gere_faturas
import historico_faturas

def main():
    st.title("Aplicação Orçamento - Contas Mãe")
    st.image("caminho_para_sua_imagem/foto_benedita.png", use_column_width=True)

    menu = st.sidebar.selectbox(
        "Escolha uma opção:",
        ["Menu Principal", "Gerir Faturas", "Histórico de Faturas"]
    )

    if menu == "Menu Principal":
        st.subheader("Bem-vindo ao Gerenciador de Orçamento")
    elif menu == "Gerir Faturas":
        gere_faturas.insert()
    elif menu == "Histórico de Faturas":
        historico_faturas.show()

if __name__ == "__main__":
    main()
