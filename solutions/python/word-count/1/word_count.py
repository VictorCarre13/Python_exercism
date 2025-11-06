from collections import Counter
import re
def count_words(sentence):
    sentence=sentence.replace("_"," ")
    pattern = r"\b\w+(?:'\w+)?\b"
    words = re.findall(pattern, sentence.lower())
    return dict(Counter(words))