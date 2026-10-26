from chatbot.custom_agents import start_agent
import streamlit as st
import time
# from dotenv import load_dotenv

if "history" not in st.session_state:
    # load_dotenv()  
    st.session_state.history = []

for message in st.session_state.history:
    type = message.get("role", None) or message.get("type", None)

    match type:
        case 'user': 
            with st.chat_message(type):
                st.markdown(message["content"])
        case 'assistant': 
            with st.chat_message(type):
                st.markdown(message["content"][0]["text"])
        case 'function_call': 
            if "transfer_to" not in message["name"]: 
                with st.chat_message(name="tool", avatar=":material/build:"):
                        st.markdown(f'LLM chamando tool {message["name"]}')
                        with st.expander("Visualizar argumentos"):
                            st.code(message["arguments"])
        case 'function_call_output':
            try:
                obj = json.loads(message['output'])
                with st.chat_message(name="tool", avatar=":material/data_object:"):
                    with st.expander("Visualizar resposta"):
                        st.code(obj["text"])
            except:
                continue

start_agent()

prompt = st.chat_input("Digite sua pergunta:")

if prompt:
    # Exibe a mensagem do usuário na interface do chat
    with st.chat_message("user"):
        st.markdown(prompt)

    # Adiciona a mensagem do usuário ao histórico
    st.session_state.history.append({
        "role": "user", 
        "content": prompt
    })
