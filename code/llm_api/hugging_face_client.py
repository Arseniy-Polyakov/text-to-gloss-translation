from openai import OpenAI

def hugging_face_model(model: str, system_prompt: str, user_prompt: str, HF_TOKEN: str):
    """
    Docstring for hugging_face_model
    
    :param model: HF model's name
    :type model: str
    :param system_prompt: System prompt for text-to-gloss translation
    :type system_prompt: str
    :param user_prompt: Sentences for translation
    :type user_prompt: str
    :param HF_TOKEN: TOKEN for OAUTH2
    :type HF_TOKEN: str
    """
    client = OpenAI(
        base_url="https://router.huggingface.co/v1",
        api_key=HF_TOKEN
    )
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt}, 
            {"role": "user", "content": user_prompt}
        ]
    )
        
    tokens = completion.usage.total_tokens
    answer = completion.choices[0].message.content
    print("ОТВЕТ ОТ МОДЕЛИ", answer)
    print("----------------------------")
    print("КОЛИЧЕСТВО ЗАДЕЙСТВОВАННЫХ ТОКЕНОВ HUGGING FACE: ", tokens)