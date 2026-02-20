import json
import requests

def getting_token_gigachat(TOKEN: str) -> str:
    """
    Docstring for getting_token_gigachat
    
    :param TOKEN: Authorization ID in Sber Client
    :type TOKEN: str
    :return: ACCESS TOKEN for OAUTH2 
    :rtype: str
    """
    url_token = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth" 
    headers_token = {
        "Content-Type": "application/x-www-form-urlencoded", 
        "Accept": "application/json",
        "Authorization": "Basic " + TOKEN, 
        "RqUID": "bbf6a909-6584-41bf-8ef2-eb496f9d36c3"
    }
    payload_token = {
        "scope": "GIGACHAT_API_PERS"
    }

    response_token = requests.post(url_token, headers=headers_token, data=payload_token, verify=False)
    if response_token.status_code != 200:
        print(f"Ошибка в получении ACCESS TOKEN. Статус {response_token.status_code}")
    else:
        ACCESS_TOKEN = response_token.json()["access_token"]
        return ACCESS_TOKEN

def get_models_giga(TOKEN: str) -> list:
    """
    Docstring for get_models_giga
    
    :param TOKEN: ACCESS TOKEN for OAUTH2
    :type TOKEN: str
    :return: The list of avaliable GigaChat models in your account
    :rtype: list
    """
    url_get_models = "https://gigachat.devices.sberbank.ru/api/v1/models"
    headers_get_models = {
        "Content-Type": "application/json", 
        "Authorization": "Bearer " + TOKEN
    }
    response_models = requests.get(url_get_models, headers=headers_get_models, verify=False)
    if response_models.status_code != 200:
        error = f"Ошибка в получении списка моделей GigaChat, доступных по REST API. Статус {response_models.status_code}"
        return error
    else:
        answer_models = response_models.json()["data"]
        return answer_models
    
def giga_call(model: str, system_prompt: str, user_prompt: str, TOKEN: str) -> str:
    """
    Docstring for giga_call
    
    :param model: GigaChat model's name
    :type model: str
    :param system_prompt: System Prompt for text-to-gloss translation
    :type system_prompt: str
    :param user_prompt: Sentences for translation
    :type user_prompt: str
    :param TOKEN: ACCESS TOKEN for OAUTH2
    :type TOKEN: str
    :return: Translated sentences (Gloss sequences)
    :rtype: str
    """
    url_giga = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"
    headers_giga = {
        "Content-Type": "application/json", 
        "Authorization": "Bearer " + TOKEN
    }
    payload_giga = {
        "model": model, 
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    }
    response_giga = requests.post(url_giga, headers=headers_giga, data=json.dumps(payload_giga), verify=False)
    if response_giga.status_code != 200:
        print(f"Ошибка при вызове LLM. Статус {response_giga.status_code}")
    else:
        answer_giga = response_giga.json()["choices"][0]["message"]["content"]
        return answer_giga

def monitoring_sber(TOKEN: str, system_prompt: str, user_prompt: str, answer_models: str, model: str) -> str:
    """
    Docstring for monitoring_sber
    
    :param TOKEN: ACCESS TOKEN for OAUTH2
    :type TOKEN: str
    :param system_prompt: System Prompt for text-to-gloss translation
    :type system_prompt: str
    :param user_prompt: Sentences for translation
    :type user_prompt: str
    :param answer_models: Translated sentences (Gloss Sequences)
    :type answer_models: str
    :param model: GigaChat model's name
    :type model: str
    :return: Statistics on tokens used
    :rtype: str
    """
    url_monitoring = "https://gigachat.devices.sberbank.ru/api/v1/tokens/count"
    headers_monitoring = {
        "Content-Type": "application/json", 
        "Authorization": "Bearer " + TOKEN
    }
    payload_monitoring = {
        "model": model, 
        "input": [system_prompt + user_prompt + answer_models]
    }
    response_monitoring = requests.post(url_monitoring, headers=headers_monitoring, data=json.dumps(payload_monitoring), verify=False)
    if response_monitoring.status_code != 200:
        error = f"Ошибка вызова ручки по подсчету количества использованных токенов. Статус {response_monitoring.status_code}"
        return error
    else:
        tokens_used = response_monitoring.json()[0]["tokens"]
        url_balance = "https://gigachat.devices.sberbank.ru/api/v1/balance"
        response_balance = requests.get(url_balance, headers=headers_monitoring, verify=False)
        if response_balance.status_code != 200:
            error = f"Ошибка вызова ручки остатка токенов модели. Статус {response_balance.status_code}"
            return error
        else:
            monitoring_stat = f"Использовано {tokens_used} токенов."
            return monitoring_stat
