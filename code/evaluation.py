import pandas as pd
import evaluate

def strip_function(text: str) -> str:
    """
    Docstring for strip_function
    
    :param text: Sentences
    :type text: str
    :return: Preprocessed sentences (without \s signs in both pre and post positions)
    :rtype: str
    """
    return text.strip()

def evaluate_function_bleu(file_name: str) -> list:
    """
    Docstring for evaluate_function_bleu
    
    :param file_name: File name with final glosses (the result of text-to-gloss translation)
    :type file_name: str
    :return: Bleu Score similarity
    :rtype: list
    """
    with open(file_name, "rt", encoding="utf-8") as file:
        texts_model = [line.replace("\n", "").upper() for line in file]

    df = pd.read_csv("corpora\\sentences_translations.csv")
    texts_target = df["glosses"].apply(strip_function).tolist()

    bleu_score = evaluate.load("bleu")
    bleu_final = bleu_score.compute(predictions=texts_model, references=texts_target)
    return bleu_final

file_name = "" # Enter file's name (For example: text_to_gloss_translation\\translations_glosses_to_texts\\LLM\\translation_giga_chat.txt)
print(evaluate_function_bleu(file_name))

