import spacy
from spacy.language import Language
from spacy_langdetect import LanguageDetector

# This example is using the documentation steps https://pypi.org/project/spacy-language-detection/
def get_lang_detector(nlp, name):
    return LanguageDetector()

# Here we use the pipeline structure of spaCy 
nlp = spacy.load("en_core_web_sm")
Language.factory("language_detector", func=get_lang_detector)
nlp.add_pipe('language_detector', last=True)

doc = nlp("This is an english text. El texto está en español. Ce texte est en français. Dies ist ein deutscher Text. Este es un texto en español. Das ist ein deutscher Text. Cette phrase est en français.")
print(doc._.language) # The output will be fr object that is the last document sentence language ignoring the rest of the sentences

# Document level language detection
def detect_language(doc, multi_sentence = False):
    print(multi_sentence)
    if multi_sentence:
        languages_array = []
        for i, sent in enumerate(doc.sents):
            languages_array.append(sent._.language["language"])

        return languages_array
    return doc._.language["language"] # The output will be en object


def detect_language2(text:str, multi_sentence = False):
    doc = nlp(text)
    if multi_sentence:
        languages_array = []
        for i, sent in enumerate(doc.sents):
            languages_array.append(sent._.language["language"])

        return languages_array
    return doc._.language["language"] # The output will be en object

# Sentence level language detection
for i, sent in enumerate(doc.sents):
    print(sent, sent._.language) # This iterate over each sentence and extracts the language of that sentence


# palabras_clave = [token.text for token in doc if token.pos_ in ("NOUN", "VERB")]
# palabras_clave2 = [token.text for token in doc if token.dep_ in ("nsubj", "obj", "ROOT")]
# palabras_clave3 = [token.text for token in doc if not token.is_stop and token.pos_ in ("NOUN", "VERB")]
# palabras_clave4 = [token.lemma_ for token in doc if not token.is_stop and token.pos_ in ("NOUN", "VERB")]

# print(palabras_clave)
# print(palabras_clave2)
# print(palabras_clave3)
# print(palabras_clave4)

# for token in doc:
#     print(token.text, token.lemma_, token.pos_, token.dep_, token.shape_, token.is_alpha, token.is_stop)

# def find_answer(text, data):
#   doc