import json
import requests

def yandex_gpt_api_main(model_uri: str, TOKEN: str, system_prompt: str, user_prompt: str):
    """
    Docstring for yandex_gpt_api
    
    :param model_uri: Yandex AI Studio LLM's uri
    :type model_uri: str
    :param TOKEN: API KEY for OAUTH2 (from Identity and Service Management)
    :type TOKEN: str
    :param system_prompt: System prompt for text-to-gloss translation
    :type system_prompt: str
    :param user_prompt: Sentences for translation
    :type user_prompt: str
    """
    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json", 
        "Authorization": "Api-Key " + TOKEN
    }
    data = {
        "modelUri": model_uri, 
        "messages": [
            {"role": "system", "text": system_prompt}, 
            {"role": "user", "text": user_prompt}
        ]
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code != 200:
        print("СТАТУС: ", response.status_code)
        print(response.json())
    else:
        response_json = response.json()
        model_answer = response_json["result"]["alternatives"][0]["message"]["text"]
        tokens_used = response_json["result"]["usage"]["totalTokens"]
        print("ОТВЕТ ОТ МОДЕЛИ", model_answer)
        print()
        print("КОЛИЧЕСТВО ИСПОЛЬЗУЕМЫХ ТОКЕНОВ", tokens_used)

def yandex_gpt_foreign(TOKEN: str, FOLDER_ID: str, model: str, system_prompt: str, user_prompt: str) -> dict:
    """
    Docstring for yandex_gpt_foreign
    
    :param TOKEN: API KEy for OUATH2 (from Identity and Access Management)
    :type TOKEN: str
    :param FOLDER_ID: FOLDER ID for OPEN AI
    :type FOLDER_ID: str
    :param model: Yandex AI Studio LLM's name
    :type model: str
    :param system_prompt: System prompt for text-to-gloss translation
    :type system_prompt: str
    :param user_prompt: Sentences for translation
    :type user_prompt: str
    :return: LLM's answer in JSON (with translated sentences)
    :rtype: dict
    """
    url = "https://rest-assistant.api.cloud.yandex.net/v1/responses"
    headers = {
        "Content-Type": "application/json", 
        "Authorization": "Api-Key " + TOKEN, 
        "OpenAI-Project": FOLDER_ID
    }
    data = {
        "model": model, 
        "instructions": system_prompt, 
        "input": user_prompt, 
        "temperature": 0.3, 
        "max_output_tokens": 2000
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()