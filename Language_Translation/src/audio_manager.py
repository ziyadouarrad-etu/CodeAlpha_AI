import io
from gtts import gTTS
import streamlit as st

class AudioManager:
    @staticmethod
    def play_audio(text, lang_code):
        try:
            fixed_code = 'ja' if lang_code == 'jp' else lang_code
            tts = gTTS(text=text, lang=fixed_code)
            
            fp = io.BytesIO()
            tts.write_to_fp(fp)
            
            st.audio(fp.getvalue(), format="audio/mp3", autoplay=True)
        except Exception as e:
            st.error(f"Audio Error: {e}")