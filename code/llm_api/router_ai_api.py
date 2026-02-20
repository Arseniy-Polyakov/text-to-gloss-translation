import json
import requests

def router_ai(TOKEN: str, model: str, system_prompt: str, user_prompt: str) -> tuple:
    """
    Docstring for open_router
    
    :param TOKEN: Router AI TOKEN for OAUTH2
    :type TOKEN: str
    :param model: LLM's name
    :type model: str
    :param system_prompt: System prompt for text-to-gloss translation
    :type system_prompt: str
    :param user_prompt: Sentences for translation
    :type user_prompt: str
    :return: Translated sentences (Gloss sequences) and tokens used
    :rtype: tuple
    """
    url = "https://routerai.ru/api/v1/chat/completions"
    headers = {
        "Content-Type": "application/json", 
        "Authorization": "Bearer " + TOKEN
    }
    data = {
        "model": model, 
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ] 
    }
    response = requests.post(url, headers=headers, data=json.dumps(data)).json()
    model_answer = response["choices"][0]["message"]["content"]
    tokens = response["usage"]["total_tokens"]
    return model_answer, tokens