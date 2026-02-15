import streamlit as st
from src.translator import GeminiTranslator

class PageManager:
    @staticmethod
    def initialize_state():
        """Sets up all session state variables."""
        if 'translator' not in st.session_state:
            st.session_state.translator = GeminiTranslator()
        if 'translation_result' not in st.session_state:
            st.session_state.translation_result = None

    @staticmethod
    def render_sidebar():
        """Renders the sidebar and returns the debug mode status."""
        with st.sidebar:
            st.title("⚙️ Settings")
            # We use a key here to ensure it's stored in session_state automatically
            debug = st.toggle("Debug / Mock Mode", value=True, key="debug_toggle")
            if debug:
                st.info("Mock Mode is ON.")
            return debug