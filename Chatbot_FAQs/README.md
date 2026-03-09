# 🤖 NLP-Powered FAQ Chatbot

A retrieval-based chatbot that answers frequently asked questions using **Natural Language Processing (NLP)** and **Vector Similarity** instead of simple keyword matching.

---

# 📌 Project Overview

This chatbot uses **TF-IDF vectorization** and **cosine similarity** to analyze the semantic similarity between user queries and a knowledge base of frequently asked questions.

Instead of relying on basic keyword matching, the system converts text into vectors and identifies the most relevant response based on **mathematical similarity scores**.

This approach significantly improves accuracy when users phrase questions in different ways.

---

# 🛠️ Technical Stack

- **Language:** Python
- **NLP:** NLTK (Natural Language Toolkit)
- **Machine Learning:** Scikit-learn
  - TF-IDF Vectorization
  - Cosine Similarity
- **Web Framework:** Streamlit
- **Data Storage:** JSON

---

# 🚀 Key Features

### Intelligent Matching

Uses **TF-IDF Vectorization** and **Cosine Similarity** to retrieve the most relevant answer based on vector similarity rather than exact text matching.

---

### NLP Preprocessing Pipeline

Uses **NLTK** for advanced text preprocessing:

- Tokenization
- Stopword removal
- Lemmatization

This cleaning pipeline improves the **signal-to-noise ratio** of user queries.

---

### Confidence Thresholding

Applies a **similarity threshold (0.7)** before returning an answer.

If the similarity score is below this threshold, the chatbot avoids responding with incorrect information.

This helps reduce **low-confidence matches and hallucinations**.

---

### Observability Dashboard

Includes a **Debug Mode** that displays similarity scores for all potential matches.

This allows developers to:

- Audit chatbot decisions
- Tune threshold values
- Improve dataset coverage

---

### Data Augmentation

The dataset includes **multiple question variations per intent**, improving the chatbot’s ability to recognize different phrasings of the same question.

---

# 🏗️ System Architecture

The project follows a **Modular Design Pattern** and respects the **Single Responsibility Principle**, making the system scalable and maintainable.

### Core Components

**`src/processor.py` — Text Processing Engine**

Handles the NLP preprocessing pipeline:

- tokenization
- stopword removal
- lemmatization
- NLTK resource management (`punkt_tab`)

---

**`src/search_engine.py` — Retrieval Engine**

Responsible for:

- TF-IDF vectorization
- n-gram optimizations
- cosine similarity calculations
- selecting the best answer match

---

**`src/chat_ui.py` — User Interface Layer**

Manages the **Streamlit chat interface** and maintains the conversation state between user interactions.

---

**`app.py` — Application Orchestrator**

Coordinates the full pipeline:

1. Receives user input
2. Sends text to the NLP processor
3. Passes cleaned text to the search engine
4. Displays the best response through the UI

---

# 📂 Project Structure

```

CodeAlpha_FAQ_Bot/

├── data/
│   └── faqs.json          # Knowledge base with augmented question variations
├── src/
│   ├── processor.py       # NLTK-based text cleaning logic
│   ├── search_engine.py   # TF-IDF vectorization & similarity calculations
│   └── chat_ui.py         # Streamlit UI components
├── app.py                 # Main entry point & system orchestrator
├── requirements.txt       # Project dependencies
└── .gitignore             # Excludes environments, caches, and temporary files

```

---

# 🚀 Getting Started

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/CodeAlpha_FAQ_Bot.git
cd CodeAlpha_FAQ_Bot
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Run the Application

```bash
streamlit run app.py
```

The chatbot interface will open in your browser.

---

# 📸 Demo

## ![a chat with the bot asking about joining eligability and guide](image.png)

---

# 🎯 Example Use Case

User question:

```
What programs does ENSAM offer?
```

Chatbot processing pipeline:

1. Text cleaning (NLTK)
2. Vectorization (TF-IDF)
3. Similarity comparison
4. Response retrieval

The chatbot returns the **most semantically similar FAQ response**.

---

# 👤 Author

**Ziyad Ouarrad**

AI & Computer Science Engineering Student
ENSAM Casablanca

AI & ML Trainer
GDG on Campus ENSAM CASA
