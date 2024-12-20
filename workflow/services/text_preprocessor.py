from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
import string
import re


class TextPreprocessor:
    """
    Handles text preprocessing operations including tokenization and stop word removal
    """

    def __init__(self):
        # Download required NLTK data
        try:
            nltk.data.find("tokenizers/punkt")
            nltk.data.find("corpora/stopwords")
        except LookupError:
            nltk.download("punkt")
            nltk.download("stopwords")

        self.stop_words = set(stopwords.words("english"))

    def preprocess_text(self, text):
        """
        Preprocesses text by performing the following steps:
        1. Convert to lowercase
        2. Remove punctuation
        3. Remove numbers
        4. Tokenize
        5. Remove stop words

        Args:
            text (str): Input text to preprocess

        Returns:
            dict: Dictionary containing both processed tokens and original text
        """
        # Convert to lowercase
        text = text.lower()

        # Remove punctuation
        text = text.translate(str.maketrans("", "", string.punctuation))

        # Remove numbers
        text = re.sub(r"\d+", "", text)

        # Tokenize
        tokens = word_tokenize(text)

        # Remove stop words
        filtered_tokens = [token for token in tokens if token not in self.stop_words]

        return {
            "original_text": text,
            "processed_tokens": filtered_tokens,
            "token_count": len(filtered_tokens),
        }
