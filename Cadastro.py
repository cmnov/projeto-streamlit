import streamlit as st
import pandas as pd
from datetime import date

#Funcao para validar se nome e dt_nascimento esta prenchidos e gravar dados
def gravar_dados(nome, dt_nascimento, tipo):
    if nome and dt_nascimento <= date.today():
        with open("clientes.csv","a",encoding="utf-8") as file:
            file.write(f"{nome},{dt_nascimento},{tipo}\n")
        st.session_state["sucesso"] = True
    else:
        st.session_state["sucesso"] = False



st.set_page_config(
    page_title="Cadastro de clientes",
    page_icon="📖"
)

st.title("Cadastro de clientes")
st.divider()

nome = st.text_input("Digite nome do cliente",
                     key="nome_cliente")

dt_nascimento = st.date_input("Data nascimento", format="DD/MM/YYYY")

tipo_cliente = st.selectbox("Tipo do cliente", 
                            ["Pessoa Juridica", "Pessoa Fisica"])

btn_cadastrar = st.button("Cadastrar",
                          on_click=gravar_dados, 
                          args=[nome, dt_nascimento, tipo_cliente])

if btn_cadastrar:
    if st.session_state["sucesso"]:
        st.success("Cliente cadastrado com sucesso",
                   icon="✅")
    else:
        st.error("Falha ao criar cadastro", 
                 icon="😭")   