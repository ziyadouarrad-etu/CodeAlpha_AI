# 🌐 AI Multilingual Translator with TTS

**CodeAlpha Internship - Task 1: Language Translation Tool**

A modular, professional-grade translation platform built with **Gemini' API**. This project demonstrates a clean separation of concerns, sophisticated state management in Streamlit, and seamless integration of Multimodal AI and Text-to-Speech (TTS) technologies.

---

## 🚀 Key Features

* **Context-Aware Translation:** Powered by Gemini's API for nuanced, high-fidelity translations.
* **Automatic Language Detection (ALD):** Uses zero-shot AI classification to identify source languages instantly.
* **Native Text-to-Speech:** Integrated `gTTS` engine providing localized audio for both original and translated text.
* **In-Memory Processing:** Audio is handled via `io.BytesIO` streams, ensuring high performance without local file overhead.
* **Clipboard Integration:** One-click copy functionality for streamlined user workflows.
* **Developer Mock Mode:** A built-in mocking layer to allow UI/UX testing while preserving API rate limits.

---

## 📸 Screenshot
<img width="1600" height="738" alt="image" src="https://github.com/user-attachments/assets/3b874286-a911-4f8f-a366-a00eb02dae3d" />


---

## 🏗️ Technical Architecture

The project follows a **Modular Design Pattern**, ensuring that each component has a single responsibility. This makes the codebase highly maintainable and easy to scale.

* **`app.py`**: The Orchestrator. Manages the main execution flow and Streamlit page lifecycle.
* **`src/translator.py`**: The AI Engine. Handles prompt engineering, `response_schema` enforcement, and API mocking logic.
* **`src/audio_manager.py`**: The Sound Engine. Manages gTTS logic and byte-stream audio playback.
* **`src/page_manager.py`**: The State Manager. Synchronizes the sidebar settings and `st.session_state` variables.
* **`src/ui_components.py`**: The View Layer. Contains the layout definitions and interactive widgets (buttons, badges, results).
---

## 📂 Project Structure
The repository is organized into a main entry point and a src/ directory containing the modularized logic:

Plaintext
```
CodeAlpha_Language_Translation/
├── main.py                 # Entry point (Streamlit Orchestrator)
├── .env                    # Environment variables (API Key)
├── .gitignore              # Files to exclude from Git
├── requirements.txt        # Project dependencies
├── README.md               # Documentation
└── src/                    # Source directory (Modular Logic)
    ├── __init__.py         # Makes 'src' a Python package
    ├── audio_manager.py    # TTS & Byte-stream audio handling
    ├── page_manager.py     # Session state & Sidebar management
    ├── translator.py       # Gemini API logic & Mocking layer
    └── ui_components.py    # Reusable UI widgets & Layouts
```

---

## 🛠️ Installation & Setup

### 1. Prerequisites

* Python 3.10+
* Google AI Studio API Key

### 2. Setup Environment

```bash
git clone https://github.com/your-username/CodeAlpha_Language_Translation.git
cd CodeAlpha_Language_Translation
pip install -r requirements.txt

```

### 3. Environment Variables

Create a `.env` file in the root directory:

```text
GEMINI_API_KEY=your_actual_key_here

```

### 4. Run the Application

```bash
streamlit run app.py

```

---

## ⚙️ Engineering Decisions

### **State Persistence**

Standard Streamlit scripts re-run from top-to-bottom on every interaction. To prevent the translation result from disappearing when the "Listen" button is clicked, this project implements `st.session_state` persistence.

### **API Rate-Limit Handling**

To respect the **5-RPM (Requests Per Minute)** limit of the Gemini Free Tier, a **Mock Mode** was implemented. This allows for rapid UI adjustments and layout testing without triggering `429: Quota Exceeded` errors.

---

## 📜 Dependencies

* `streamlit`: Web interface framework.
* `google-generativeai`: Gemini Pro/Flash API access.
* `gTTS`: Google Text-To-Speech library.
* `pyperclip`: Cross-platform clipboard management.
* `python-dotenv`: Environment variable management.

---

## 👤 Author

**Ouarrad Ziyad**

* **1st Year AI & CS Engineering Student** | ENSAM Casablanca
* **AI & ML Trainer** | GDG on Campus ENSAM CASA

---

## 🙏 Acknowledgments
Special thanks to CodeAlpha for providing this internship opportunity and for designing challenges that foster real-world AI and NLP skills development.
