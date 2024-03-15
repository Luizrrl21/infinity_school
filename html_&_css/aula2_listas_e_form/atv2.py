import streamlit as st

st.title("Cadastro")

col1, col2 = st.columns(2)

with col1:
    nome = st.text_input("Nome")
    celular = st.text_input("Número", placeholder="11 99999-9999")
    site = st.text_input("Seu site")
    data = st.date_input("Data Nasc")
    Qtde_filhos = st.number_input("Qtde filhos", value=int())
    sexo = st.radio("Sexo", ["Masculino", "Feminino"])

with col2:
    email = st.text_input("Email")
    horario = st.time_input("Horário")
    senha = st.text_input("Senha", type="password")
    cor = st.color_picker("Cor favorita")
    peso = st.slider("Peso", 0, 200)
    estado = st.selectbox("Estado", ["SP", "CE", "MA", "PI", "PA", "RJ"])   

mensagem = st.text_area("Mensagem")

reset = st.button("Reset")
enviar = st.button("Enviar")