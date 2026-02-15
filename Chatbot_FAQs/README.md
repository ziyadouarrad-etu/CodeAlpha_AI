# 🤖 NLP-Powered FAQ Chatbot

**CodeAlpha Internship - Task 2: Intelligent Retrieval System**

A retrieval-based chatbot that utilizes **Natural Language Processing (NLP)** and **Vector Similarity** to provide intelligent, context-aware responses to frequently asked questions. This project demonstrates a transition from basic keyword matching to a mathematical **Vector Space Model** approach.

---

## 🚀 Key Features

* **Intelligent Matching:** Employs **TF-IDF Vectorization** and **Cosine Similarity** to identify the best answer based on mathematical "closeness" rather than exact string matching.
* **NLP Preprocessing Pipeline:** Uses **NLTK** for tokenization, stopword removal, and lemmatization to clean user input and improve the signal-to-noise ratio.
* **Confidence Thresholding:** Implements a logic gate (set at 0.7) that only triggers a response if the similarity score meets a specific threshold, ensuring high-quality answers and reducing hallucinations.
* **Observability Dashboard:** Includes a dedicated **Debug Mode** to visualize similarity scores for all potential matches, allowing for precise threshold tuning and performance auditing.
* **Data Augmentation:** Features an expanded JSON dataset with multiple question variations per intent to increase matching reliability across diverse phrasing.

---

## 🏗️ System Architecture

The project follows a **Modular Design Pattern**, adhering to the **Single Responsibility Principle** to ensure the system is scalable and maintainable:

* **`src/processor.py`**: The Cleaning Engine. Handles the NLTK pipeline, including the recently updated `punkt_tab` resources.
* **`src/search_engine.py`**: The Brain. Manages the TF-IDF vector space, N-gram optimizations, and calculates Cosine Similarity scores.
* **`src/chat_ui.py`**: The View Layer. Manages Streamlit chat components and maintains stateful conversation history.
* **`app.py`**: The Orchestrator. Coordinates the flow between the user input, the NLP processor, and the search engine.

---

## 🛠️ Technical Stack

* **Language:** Python
* **NLP:** NLTK (Natural Language Toolkit)
* **Machine Learning:** Scikit-learn (TF-IDF, Cosine Similarity)
* **Web Framework:** Streamlit
* **Data Handling:** JSON

---

## 📂 Project Structure

```text
CodeAlpha_FAQ_Bot/
├── data/
│   └── faqs.json          # Knowledge base with augmented question variations
├── src/
│   ├── processor.py       # NLTK-based text cleaning logic
│   ├── search_engine.py   # Vectorization & Similarity calculations
│   └── chat_ui.py         # Modular Streamlit UI components
├── app.py                 # Main entry point and orchestrator
├── requirements.txt       # Project dependencies
└── .gitignore             # Exclusion rules for environment and caches

```

---

## 📸 Screenshot
<img width="1920" height="882" alt="image" src="https://github.com/user-attachments/assets/966930c2-c066-4332-8c2e-fd4b942073c7" />

---

## 👤 Author

**Ouarrad Ziyad**

* **1st Year AI & CS Engineering Student** | ENSAM Casablanca
* **AI & ML Trainer** | GDG on Campus ENSAM CASA

---

## 🙏 Acknowledgments
Special thanks to CodeAlpha for providing this internship opportunity and for designing challenges that foster real-world AI and Computer Vision skills development.
