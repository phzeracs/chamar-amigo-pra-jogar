import streamlit as st
import urllib.parse

st.set_page_config(page_title="Vai jogar hoje?", page_icon="🎮", layout="centered")

st.title("Vai jogar hoje? 🎮")

# Exibir o seletor para escolher a opção
resposta = st.selectbox("Escolha uma opção:", ["Selecione", "Sim", "Não", "Não sei"])

# Dicionário com mensagens padrão
mensagens = {
    "Sim": "Vou jogar sim, estou logando! 🎮🔥",
    "Não": "Hoje não vai rolar, fica pra próxima! 😔",
    "Não sei": "Talvez... ainda tô decidindo. 🤔"
}

# Quando a pessoa escolhe "Sim", pedimos para digitar o jogo
if resposta == "Sim":
    jogo = st.text_input("O que você deseja jogar?")

    if jogo:
        # Atualizar a mensagem com o nome do jogo
        mensagens["Sim"] = f"Sim, estava pensando em {jogo}, estou logando! 🎮🔥"

# Quando a pessoa escolhe "Não sei", pedimos para escrever uma mensagem
if resposta == "Não sei":
    mensagem_nao_sei = st.text_area("Escreva o que está pensando...", height=100)
    if mensagem_nao_sei:
        # Substitui a mensagem padrão de "Não sei" com a mensagem personalizada
        mensagens["Não sei"] = f"Talvez... ainda tô decidindo. 🤔 -> Motivo: {mensagem_nao_sei}."

# Se o usuário não selecionou "Selecione", gera o link de WhatsApp
if resposta != "Selecione":
    texto = mensagens[resposta]

    # Se a resposta for "Sim", inclui o jogo na mensagem
    if resposta == "Sim" and jogo:
        texto = f"Sim, estava pensando em {jogo}, estou logando! 🎮🔥"

    # Codificar o texto para URL corretamente, incluindo emojis
    texto_codificado = urllib.parse.quote(texto, safe=":/?&=")

    # Gerar o link do WhatsApp
    link_wpp = f"https://wa.me/?text={texto_codificado}"

    # Exibe o botão para compartilhar no WhatsApp
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
