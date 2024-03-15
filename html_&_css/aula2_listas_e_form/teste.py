import streamlit as st

st.title("teste")

usuario = st.text_input("Usuário")
idade = st.number_input(label="Idade", value=int())
email = st.text_input("Email") #Criar validação
senha = st.text_input(label="Senha", type="password")
data = st.date_input(label="Data de nascimento", format="DD/MM/YYYY")
horario = st.time_input("Horário")
cor = st.color_picker("Escolha uma cor")
arquivo = st.file_uploader("Escolha um arquivo")
barrinha = st.slider("Escolha um número")
radio = st.radio("Escolha uma opção", ["Opção 1", "Opção 2", "Opção 3"])