import os
import nltk
import pandas as pd
import evaluate
from tqdm import tqdm
from nltk.translate.bleu_score import corpus_bleu, SmoothingFunction

# nltk.download("popular")

def strip_function(text: str) -> str:
    """
    Docstring for strip_function
    
    :param text: Sentences
    :type text: str
    :rtype: str
    """
    return text.strip()

def evaluate_function_bleu(file_name: str) -> list:
    """
    Docstring for evaluate_function_bleu
    
    :param file_name: File name with final glosses (the result of text-to-gloss translation)
    :type file_name: str
    :rtype: list
    """
    with open(file_name, "rt", encoding="utf-8") as file:
        texts_model = [line.replace("\n", "").upper() for line in file]

    df = pd.read_csv("corpora\\sentences_translations.csv")
    texts_target = df["glosses"].apply(strip_function).tolist()

    bleu_score = evaluate.load("bleu")
    bleu_final = bleu_score.compute(predictions=texts_model, references=texts_target)
    return bleu_final

def ngam_bleu(file_name: str) -> dict:
    df = pd.read_csv("corpora\\sentences_translations.csv")
    texts_target = df["glosses"].apply(strip_function).tolist()
    texts_target_splitted = [[sentence.split()] for sentence in texts_target]

    with open(file_name, "rt", encoding="utf-8") as file:
        translations = [line.replace("\n", "").upper() for line in file]
    translations_splitted = [sentence.split() for sentence in translations]

    smooth = SmoothingFunction().method1
    ngram_bleu = {
        "bleu_1": round(corpus_bleu(hypotheses=translations_splitted, 
                            list_of_references=texts_target_splitted,
                            smoothing_function=smooth), 2),
        "bleu_2": round(corpus_bleu(hypotheses=translations_splitted, 
                           list_of_references=texts_target_splitted,
                           weights=(0, 1, 0, 0), 
                           smoothing_function=smooth), 2),
        "bleu_3": round(corpus_bleu(hypotheses=translations_splitted, 
                           list_of_references=texts_target_splitted,
                           weights=(0, 0, 1, 0), 
                           smoothing_function=smooth), 2),
        "bleu_4": round(corpus_bleu(hypotheses=translations_splitted, 
                           list_of_references=texts_target_splitted,
                           weights=(0, 0, 0, 1), 
                           smoothing_function=smooth), 2)
    }
    df = pd.DataFrame(ngram_bleu, index=[file_name.split("gloss_translations\\")[1:]], columns=ngram_bleu.keys())
    df.to_csv("ngram_bleu.csv", sep=";", header=False, mode="a")
    return df

# output = [ngam_bleu("gloss_translations\\llm\\" + file) for file in tqdm(os.listdir("gloss_translations\\llm"))]

df = pd.read_csv("ngram_bleu.csv", sep=";")
df = df.sort_values(by=["bleu_1", "bleu_2", "bleu_3", "bleu_4"])
df.to_csv("ngram_bleu.csv", sep=";")