import streamlit as st

class ChatUI:
    @staticmethod
    def render_chat_history():
        """Displays all previous messages stored in session state."""
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    @staticmethod
    def add_message(role, content):
        """Helper to add a message to history and session state."""
        st.session_state.messages.append({"role": role, "content": content})
        with st.chat_message(role):
            st.markdown(content)