import pandas as pd

def parsing_glosses() -> list:
    """
    Docstring for parsing_glosses
    
    :return: Unique Slovo dataset classes for system prompt
    :rtype: list
    """
    df = pd.read_csv("corpora\\annotations_slovo.csv", sep="\t")
    glosses_slovo = [item.upper().replace(",", "").strip() for item in df["gloss"].tolist()]
    glosess_slovo_unique = list(set(glosses_slovo))
    return glosess_slovo_unique

def parsing_texts() -> list:
    """
    Docstring for parsing_texts
    
    :return: Sentences in Russian for text-to-gloss translation
    :rtype: list
    """
    df = pd.read_csv("corpora\\sentences_translations.csv")
    russian_texts = df["russian"].tolist()
    return russian_texts

def parsing_texts_glosses() -> list: 
    """
    Docstring for parsing_texts_glosses
    
    :return: Target gloss translations of sentences in Russian
    :rtype: list
    """
    df = pd.read_csv("corpora\\sentences_translations.csv")
    texts_glosses = df["glosses"].tolist()
    return texts_glosses

