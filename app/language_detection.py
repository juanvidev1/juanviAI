import spacy
from spacy.language import Language
from spacy_langdetect import LanguageDetector

def get_lang_detector(nlp, name):
    return LanguageDetector()

nlp = spacy.load("en_core_web_sm")
Language.factory("language_detector", func=get_lang_detector)
nlp.add_pipe('language_detector', last=True)

def detect_language(text:str, multi_sentence = False):
    doc = nlp(text)
    if multi_sentence:
        languages_array = []
        for i, sent in enumerate(doc.sents):
            languages_array.append(sent._.language)

        return languages_array
    return doc._.language # The output will be en object