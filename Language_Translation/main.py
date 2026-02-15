import streamlit as st
from src.page_manager import PageManager
from src.audio_manager import AudioManager
from src.ui_components import UIComponents

# 1. Setup & State
PageManager.initialize_state()
debug_mode = PageManager.render_sidebar()
audio_mgr = AudioManager()

st.title("🌐 AI Language Translator")

# 2. Input Section
with st.container():
    col1, col2 = st.columns([3, 1])
    with col1:
        text_input = st.text_area("Source Text", placeholder="Type here...", height=150)
    with col2:
        target_lang = st.selectbox("Target Language", ["French", "Arabic", "Spanish", "German", "Japanese"])

# 3. Execution
if st.button("Translate ✨", use_container_width=True):
    if text_input.strip():
        engine = st.session_state.translator
        if debug_mode:
            st.session_state.translation_result = engine.get_mock_translation(text_input, target_lang)
        else:
            with st.spinner("Translating via Gemini..."):
                st.session_state.translation_result = engine.translate(text_input, target_lang)
    else:
        st.warning("Please enter some text.")

# 4. Results
if st.session_state.translation_result:
    UIComponents.display_results(
        st.session_state.translation_result, 
        target_lang, 
        audio_mgr, 
        debug_mode
    )