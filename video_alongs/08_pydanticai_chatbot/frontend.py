import streamlit as st
from chat import JokeBot

def init_session_states():
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    if "bot" not in st.session_state:
        st.session_state.bot = JokeBot()

def display_chat_messages():
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

def handel_user_input():
    if prompt := st.chat_input("Talk to the REF"):
        st.session_state.messages.append({"role": "user", "content": prompt})

        bot_response = st.session_state.bot.chat(prompt).get("bot")
        response = f"Robot: {bot_response}"

        with st.chat_message("user"):
            st.markdown(prompt)
        with st.chat_message("assistant"):
            st.markdown(response)
        
        st.session_state.messages.append({"role": "assistant", "content": response})

def layout():
    st.markdown("# Chat with REF ")
    st.write(
        "Ref is a sports referee. He is a real sports freak ask whatever and he will knew it!"
    )

    display_chat_messages()
    handel_user_input()

if __name__ == "__main__":
    init_session_states()
    layout()
