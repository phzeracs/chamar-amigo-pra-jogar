import streamlit as st
import urllib.parse

# Configura a página do Streamlit
st.set_page_config(page_title="Vai jogar hoje?", page_icon="🎮", layout="centered")

# Título da página
st.title("Vai jogar hoje? 🎮")

# Exibe a pergunta com opções
resposta = st.selectbox("Escolha uma opção:", ["Selecione", "Sim", "Não", "Não sei"])

# Mensagens padrão para cada opção
mensagens = {
    "Sim": "Vou jogar sim, estou logando! 🎮🔥",
    "Não": "Hoje não vai rolar, fica pra próxima! 😔",
    "Não sei": "Talvez... ainda tô decidindo. 🤔"
}

# Variável que vai guardar a mensagem final para o WhatsApp
texto = ""

# Se a resposta for "Sim", pergunta o que a pessoa quer jogar
if resposta == "Sim":
    jogo = st.text_input("O que vamos jogar hoje?")

    # Se escreveu o jogo, cria a mensagem com o nome do jogo
    if jogo.strip():
        texto = f"Sim, estava pensando em {jogo.strip()}, estou logando! 🎮🔥"

# Se a resposta for "Não", usa a mensagem padrão
elif resposta == "Não":
    texto = mensagens["Não"]

# Se a resposta for "Não sei"
elif resposta == "Não sei":
    # Opção para decidir se vai usar mensagem personalizada ou padrão
    modo_msg = st.radio("Deseja enviar uma mensagem personalizada?", ["Mensagem automática", "Mensagem personalizada"])

    # Se escolheu personalizada, mostra a caixa de texto
    if modo_msg == "Mensagem personalizada":
        mensagem_nao_sei = st.text_area("Escreva o motivo, se quiser.. ", height=100)

        # Se escreveu algo, atualiza a mensagem
        if mensagem_nao_sei.strip():
            texto = f"Talvez... ainda tô decidindo. 🤔 {mensagem_nao_sei.strip()}."
    else:
        # Se escolheu automática, mantém a mensagem padrão
        texto = mensagens["Não sei"]

# Só gera o botão do WhatsApp se uma opção válida foi escolhida e a mensagem não estiver vazia
if resposta != "Selecione" and texto:
    # Codifica o texto para a URL, para funcionar com acentos e emojis
    texto_codificado = urllib.parse.quote(texto, safe=":/?&=")

    # Monta o link do WhatsApp
    link_wpp = f"https://wa.me/?text={texto_codificado}"

    # Mostra um botão customizado que leva pro WhatsApp
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
