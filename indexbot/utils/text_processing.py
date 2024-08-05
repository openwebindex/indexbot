from rake_nltk import Rake
from gensim.summarization import summarize

def extract_keywords(content):
    rake = Rake()
    try:
        rake.extract_keywords_from_text(content)
        return rake.get_ranked_phrases()
    except:
        return []

def generate_summary(content, word_count=100):
    try:
        return summarize(content, word_count=word_count)
    except ValueError:
        return "Summary could not be generated."
