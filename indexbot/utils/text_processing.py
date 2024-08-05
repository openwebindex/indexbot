import nltk
from rake_nltk import Rake
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

nltk.download("stopwords")

def extract_keywords(content):
    rake = Rake()
    try:
        rake.extract_keywords_from_text(content)
        return rake.get_ranked_phrases()
    except:
        return []

def generate_summary(content, sentences=3):
    try:
        # Parse the text & generate the summary
        parser = PlaintextParser.from_string(content, Tokenizer("english"))
        summarizer = LsaSummarizer()
        summary = summarizer(parser.document, sentences)
    except:
        return None
