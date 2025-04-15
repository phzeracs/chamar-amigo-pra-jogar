import streamlit as st
import urllib.parse

# Configura a página do Streamlit
st.set_page_config(page_title="Vai jogar hoje?", page_icon="🎮", layout="centered")

# Título da página
st.title("Vai jogar hoje? 🎮")

# Pergunta principal
resposta = st.selectbox("Escolha uma opção:", ["Selecione", "Sim", "Não", "Não sei"])

# Mensagens padrão
mensagens = {
    "Sim": "Vou jogar sim, estou logando! 🎮🔥",
    "Não": "Hoje não vai rolar, fica pra próxima! 😔",
    "Não sei": "Talvez... ainda tô decidindo. 🤔"
}

# Mensagem final que será enviada no WhatsApp
texto = ""

# Se escolher "Sim", pede o jogo
if resposta == "Sim":
    jogo = st.text_input("O que vamos jogar hoje?")
    if jogo.strip():
        texto = f"Sim, estava pensando em {jogo.strip()}, estou logando! 🎮🔥"

# Se escolher "Não", usa a mensagem padrão
elif resposta == "Não":
    texto = mensagens["Não"]

# Se escolher "Não sei", permite escolher entre mensagem automática ou personalizada
elif resposta == "Não sei":
    modo_msg = st.radio("Deseja enviar uma mensagem personalizada?", ["Mensagem automática", "Mensagem personalizada"])

    if modo_msg == "Mensagem personalizada":
        mensagem_nao_sei = st.text_area("Escreva o motivo, se quiser...", height=100)

        # Se escreveu algo, usa só essa mensagem (sem parte automática)
        if mensagem_nao_sei.strip():
            texto = mensagem_nao_sei.strip()
    else:
        texto = mensagens["Não sei"]

# Se a opção for válida e a mensagem estiver pronta, cria o link do WhatsApp
if resposta != "Selecione" and texto:
    texto_codificado = urllib.parse.quote(texto, safe=":/?&=")
    link_wpp = f"https://wa.me/?text={texto_codificado}"

    # Botão estilizado para abrir o WhatsApp
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
