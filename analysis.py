import spacy
from collections import Counter

nlp = spacy.load('en_core_web_sm')

def analyze_text(text: str) -> dict:
    """Analyze text to extract entities and keywords using spaCy."""
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    keywords = [token.text for token in doc if token.pos_ in ('NOUN', 'PROPN') and not token.is_stop]
    keyword_freq = Counter(keywords)
    top_keywords = [word for word, freq in keyword_freq.most_common(10)]
    return {
        'entities': entities,
        'keywords': top_keywords
    }