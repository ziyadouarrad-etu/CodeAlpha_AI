import streamlit as st
from src.search_engine import FAQSearchEngine
from src.chat_ui import ChatUI

# 1. Page Configuration
st.set_page_config(page_title="GDG FAQ Bot", page_icon="🤖")
st.title("🤖 GDG Campus FAQ Bot")

# 2. Initialize Engine & State
if 'engine' not in st.session_state:
    st.session_state.engine = FAQSearchEngine(data_path="data/faqs.json")

if 'messages' not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I'm the GDG ENSAM Bot. Ask me anything about our club!"}
    ]

# 3. Render Historical Chat
ChatUI.render_chat_history()

# 4. Debug Mode Toggle
debug_mode = st.sidebar.checkbox("Enable Debug Mode", value=False)

# 5. Handle User Input
if prompt := st.chat_input("Ask a question..."):
    ChatUI.add_message("user", prompt)
    
    with st.spinner("Calculating Similarity..."):
        result = st.session_state.engine.get_response(prompt, threshold=0.4)
        
    ChatUI.add_message("assistant", result["answer"])

    # --- Debugging Section ---
    if debug_mode:
        with st.expander("📊 Similarity Score Breakdown"):
            st.write(f"**Top Match:** {result['match'] if result['match'] else 'None (Below Threshold)'}")
            st.write(f"**Top Confidence:** {result['confidence']}")
            
            # Display all scores in a clean table
            st.table(result["all_scores"])