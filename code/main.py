import os
from dotenv import load_dotenv

from parsing_data import parsing_glosses, parsing_texts
from llm_api.giga_chat_api import (getting_token_gigachat, 
                       giga_call,
                       monitoring_sber)
from llm_api.hugging_face_client import hugging_face_model
from llm_api.router_ai_api import router_ai
from llm_api.yandex_gpt_api import yandex_gpt_api_main, yandex_gpt_foreign

load_dotenv()

system_prompt = f"""Ты переводчик с русского вербального языка на язык глоссов русского жестового языка.
Глоссы - это значения жестов русского жестового языка.
Список существующих глоссов русского жестового языка, используй только их для перевода: {parsing_glosses()}. 

Твоя задача - перевести предложения с русского вербального языка на глоссы русского жестового языка. 
В ответе ты должен использовать только предоставленные глоссы, никакие другие слова глоссы использовать нельзя.
Используй только глоссы в той грамматической форме, в которой они есть в списке, не меняй форму глоссов.
Используй верхний регистр для записи глоссов.
Пиши каждое новое предложение с новой строки, используй нумерованный список в ответе.
Не пиши комментарии и дополнительную информацию в ответе.

Примеры формата вывода ответа: 
Тексты на русском вербальном языке:
Испуганная девочка съёжилась от страха
Кролики любят лакомиться
Огромный медведь был на солнце после зимней спячки
Цветовая гамма весеннего пейзажа радует глаз
Купи питьевой воды

Перевод на глоссы:
1. ИСПУГАННЫЙ ДЕВОЧКА ИСПЫТЫВАТЬ СТРАХ
2. КРОЛИК ЛЮБИТЬ ЕСТЬ 
3. БОЛЬШОЙ МЕДВЕДЬ БЫТЬ СОЛНЦЕ 
4. ЦВЕТОВОЙ ОТТЕНОК ВЕСНА ПРИЯТНЫЙ ГЛАЗ
5. КУПИТЬ ПИТЬЕВАЯ ВОДА
"""

user_prompt = f"Тексты для перевода: {parsing_texts()}"

# Giga Chat Call
model_giga_chat = "" # Enter GigaChat model's name here

def giga_chat_call(model_giga_chat: str):
    model_giga_chat = ""
    ACCESS_TOKEN = getting_token_gigachat(TOKEN=os.getenv("AUTHORIZATION_ID_SBER"))
    giga_answer = giga_call(model=model_giga_chat, system_prompt=system_prompt, user_prompt=user_prompt, TOKEN=ACCESS_TOKEN)
    monitoring_check = monitoring_sber(TOKEN=ACCESS_TOKEN, model=model_giga_chat, system_prompt=system_prompt, user_prompt=user_prompt, answer_models=giga_answer)
    print("MODEL'S ANSWER", giga_answer)
    print("----------------------------")
    print(monitoring_check)

giga_chat_call()

# Yandex AI Studio LLM Call main
yandex_model_uri = "" # Enter your model Yandex URI
yandex_gpt_api_main(model_uri=yandex_model_uri, TOKEN=os.getenv("YANDEX_GPT_TOKEN"), system_prompt=system_prompt, user_prompt=user_prompt)

# Yandex AI Studio LLM Call foreign
model_yandex = "" # Enter Yandex AI Studio LLM's name here
print(yandex_gpt_foreign(TOKEN=os.getenv("YANDEX_GPT_TOKEN"), 
                        FOLDER_ID=os.getenv("FOLDER_ID"), 
                        model=model_yandex,
                        system_prompt=system_prompt, 
                        user_prompt=user_prompt))

# HF Client Call
model_hf = "" # Enter HF LLM's name
hugging_face_model(model=model_hf, 
                   system_prompt=system_prompt, 
                   user_prompt=user_prompt, 
                   HF_TOKEN=os.getenv("HF_TOKEN"))

# Router AI Call
model_router_ai = "" # Enter Router AI model's name
def open_router_call():
    open_router_call_result = router_ai(TOKEN=os.getenv("ROUTER_AI"), 
                                        model=model_router_ai, 
                                        system_prompt=system_prompt, 
                                        user_prompt=user_prompt)
    model_answer, tokens = open_router_call_result[0], open_router_call_result[1]
    print("MODEL'S ANSWER: ", model_answer)
    print()
    print("TOKENS USED", tokens)

open_router_call()