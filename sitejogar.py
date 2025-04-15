import streamlit as st
import urllib.parse

st.set_page_config(page_title="Vai jogar hoje?", page_icon="🎮", layout="centered")

st.title("Vai jogar hoje? 🎮")

resposta = st.selectbox("Escolha uma opção:", ["Selecione", "Sim", "Não", "Não sei"])

mensagens = {
    "Sim": "Vou jogar sim, estou logando! 🎮🔥",
    "Não": "Hoje não vai rolar, fica pra próxima! 😔",
    "Não sei": "Talvez... ainda tô decidindo. 🤔"
}

texto = ""

if resposta == "Sim":
    jogo = st.text_input("O que você deseja jogar?")
    if jogo.strip():
        texto = f"Sim, estava pensando em {jogo.strip()}, estou logando! 🎮🔥"

elif resposta == "Não":
    texto = mensagens["Não"]

elif resposta == "Não sei":
    mensagem_nao_sei = st.text_area("Escreva o motivo, se quiser...", height=100)
    if mensagem_nao_sei.strip():
        texto = f"Talvez... ainda tô decidindo. 🤔 -> Motivo: {mensagem_nao_sei.strip()}."
    else:
        texto = mensagens["Não sei"]

# Se uma opção válida foi escolhida e temos o texto pronto
if resposta != "Selecione" and texto:
    texto_codificado = urllib.parse.quote(texto, safe=":/?&=")
    link_wpp = f"https://wa.me/?text={texto_codificado}"

    st.markdown(f"""
        <a href="{link_wpp}" target="_blank">
            <button style="
                background-color:#25D366;
                color:white;
                border:none;
                padding:10px 20px;
                border-radius:10px;
                font-size:18px;
                cursor:pointer;
                margin-top:20px;
            ">
                📲 Compartilhar no WhatsApp
            </button>
        </a>
    """, unsafe_allow_html=True)
