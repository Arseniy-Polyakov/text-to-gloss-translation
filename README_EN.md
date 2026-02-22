# Automatic Machine Translation from Spoken-Language Text to Sign Language Gloss Sequences

## [Russian](README.md)

This work is devoted to a method of automatic machine translation of texts into glosses (translations of signs into words and phrases of a verbal language). As part of the method, a parallel corpus of Russian-language sentences was compiled and manually annotated [link](corpora/sentences_translations.csv). For annotation, a portion of the Russian Sign Language corpus Slovo [Kaggle](https://www.kaggle.com/datasets/kapitanov/slovo), specifically the file annotations.csv [link](corpora/annotations_slovo.csv), made publicly available, was used. This parallel corpus was employed to train transformer models and large language models in accordance with the proposed method. The functional diagram of the method is presented below:

<img width="1092" height="772" alt="Pipeline of the proposed method" src="https://github.com/user-attachments/assets/471e0272-00a1-49c6-a98e-77f6614e896a" />

## Experimental results for ``spoken-language text-gloss sequence`` translation task using LLMs

| Rank | Model                                  | Tokens | BLEU     |
|------|----------------------------------------|--------|----------|
| 1    | allenai/Olmo-3.1-32B-Instruct          | 27 460 | 0.06     |
| 2    | meta-llama/Llama-3.3-70B-Instruct      | 20 686 | 0.12     |
| 3    | meta-llama/Llama-3.1-8B-Instruct       | 20 685 | 0.16     |
| 4    | openai/gpt-oss-120b                    | 30 676 | 0.17     |
| 5    | GigaChat-Plus                          | 17 127 | 0.24     |
| 6    | GigaChat-2                             | 17 112 | 0.25     |
| 7    | yandex-gpt-5lite                       | 13 592 | 0.27     |
| 8    | GigaChat-2-Pro                         | 16 978 | 0.27     |
| 9    | GigaChat-2-Max                         | 17 088 | 0.33     |
| 10   | aliceai-llm                            | 13 570 | 0.33     |
| 11   | CohereLabs/command-a-reasoning-08-2025 | 24 788 | 0.36     |
| 12   | Qwen/Qwen3-32B                         | 28 245 | 0.27     |
| 13   | google/gemma-3-27b-it                  | 18 416 | 0.27     |
| 14   | deepseek-ai/DeepSeek-V3-0324           | 20 582 | 0.39     |
| 15   | openai/gpt-5.2                         | 27 238 | **0.60** |

## Experimental results for “spoken-language text-gloss sequence” translation task using transformer models

| Rank | Model                            | BLEU     | Epochs | Steps | train_runtime | samples/sec | steps/sec | train_loss (last) |
|------|----------------------------------|----------|--------|-------|---------------|-------------|-----------|-------------------|
| 1    | Helsinki-NLP/opus-mt-ru-en       | 0.70     | 1000   | 10000 | 7285.33 s     | 10.98       | 1.37      | 0.0332            |
| 2    | facebook/nllb-200-distilled-600M | 0.83     | 250    | 2500  | 4880.46 s     | 4.10        | 0.51      | 1.0352            |
| 3    | facebook/mbart-large-50          | 0.83     | 250    | 2500  | 5039.09 s     | 3.97        | 0.50      | 0.2716            |
| 4    | mT5-small                        | **0.84** | 1000   | 10000 | 5442.78 s     | 14.70       | 1.84      | 0.7575            |

Based on the data obtained, the Slovo corpus glosses were marked up. Part of the results is presented in this file [link](corpora/parallel_corpus.csv) (4340/20400). The full parallel corpus can be provided upon request.
