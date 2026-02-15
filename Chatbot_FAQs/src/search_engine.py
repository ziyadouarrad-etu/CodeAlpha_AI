import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from src.processor import TextProcessor

class FAQSearchEngine:
    def __init__(self, data_path="data/faqs.json"):
        self.processor = TextProcessor()
        self.vectorizer = TfidfVectorizer()
        
        with open(data_path, 'r') as f:
            self.raw_data = json.load(f)
        
        self.expanded_faqs = []
        self.clean_questions = []

        # Flatten the data: Every question gets its own vector but keeps the same answer
        for item in self.raw_data:
            for q in item['questions']:
                self.expanded_faqs.append({
                    "orig_q": q,
                    "answer": item['answer']
                })
                self.clean_questions.append(self.processor.clean_text(q))
        
        # Fit the vectorizer on the much larger vocabulary
        self.tfidf_matrix = self.vectorizer.fit_transform(self.clean_questions)

    def get_response(self, query, threshold=0.4): # Lowered threshold slightly for better recall
        cleaned_query = self.processor.clean_text(query)
        query_vector = self.vectorizer.transform([cleaned_query])
        
        similarities = cosine_similarity(query_vector, self.tfidf_matrix).flatten()
        
        # Get all scores for your debug table
        all_scores = [
            {"question": self.expanded_faqs[i]['orig_q'], "score": round(float(s), 4)} 
            for i, s in enumerate(similarities)
        ]
        all_scores = sorted(all_scores, key=lambda x: x['score'], reverse=True)

        best_idx = similarities.argmax()
        confidence = similarities[best_idx]
        
        # Logic remains the same, but now it matches against 20+ questions instead of 5
        if confidence >= threshold:
            return {
                "answer": self.expanded_faqs[best_idx]['answer'],
                "confidence": confidence,
                "match": self.expanded_faqs[best_idx]['orig_q'],
                "all_scores": all_scores
            }
        else:
            return {
                "answer": "I'm sorry, I couldn't find a relevant answer to your question.",
                "confidence": confidence,
                "match": None,
                "all_scores": all_scores
            }