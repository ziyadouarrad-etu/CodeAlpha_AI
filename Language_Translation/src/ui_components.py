import streamlit as st
import pyperclip

class UIComponents:
    @staticmethod
    def display_results(res, target_lang, audio_manager, debug_mode):
        st.markdown(f"**Detected:** :blue-badge[{res.get('detected_language', 'Auto')}]")
        st.success(res['translated_text'])

        # Action Buttons
        cols = st.columns([1, 1, 1, 1])
        with cols[0]:
            if st.button("🔊 Original"):
                audio_manager.play_audio(res['original_text'], res['detected_language_code'])
        with cols[1]:
            if st.button("📋 Copy Original"):
                pyperclip.copy(res['original_text'])
                st.toast("Original copied!")
        with cols[2]:
            if st.button("🔊 Translated"):
                audio_manager.play_audio(res['translated_text'], res['target_language_code'])
        with cols[3]:
            if st.button("📋 Copy Translated"):
                pyperclip.copy(res['translated_text'])
                st.toast("Translation copied!")

        # Fix: Only show if debug_mode is True
        if debug_mode:
            with st.expander("🛠️ Debug Info (JSON)"):
                st.json(res)