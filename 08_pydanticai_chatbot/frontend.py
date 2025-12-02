import streamlit as st
from chat import JokeBot

def init_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "bot" not in st.session_state:
        st.session_state.bot = JokeBot()


def display_chat():
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
        

def handel_user_input():
    
    if prompt := st.chat_input("Talk to RobotREF"):
        st.session_state.messages.append({"role": "user", "content": prompt})

        bot_response = st.session_state.bot.chat(prompt).get("bot")

        response = f"Robot: {bot_response}"

        with st.chat_message("user"):
            st.markdown(prompt)
        with st.chat_message("assistant"):
            st.markdown(response)

        st.session_state.messages.append({"role": "assistant", "content": response })

def layout():
    st.markdown("# Chat with Robot")
    st.markdown("RobotREF is a football referee!, Ask anything!")

    display_chat()
    handel_user_input()

if __name__ == "__main__":
    init_session_state()
    layout()

