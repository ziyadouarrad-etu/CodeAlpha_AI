import nltk
import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Updated download list for NLTK 3.9+ compatibility
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True) # The missing piece
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('averaged_perceptron_tagger_eng', quiet=True)

class TextProcessor:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()
        self.punctuation = string.punctuation

    def clean_text(self, text):
        """
        Pipeline: Lowercase -> Tokenize -> Remove Punctuation/Stopwords -> Lemmatize
        """
        # 1. Lowercase and Tokenize
        tokens = nltk.word_tokenize(text.lower())
        
        # 2. Filter and Lemmatize
        cleaned_tokens = [
            self.lemmatizer.lemmatize(word) 
            for word in tokens 
            if word not in self.stop_words and word not in self.punctuation
        ]
        
        return " ".join(cleaned_tokens)