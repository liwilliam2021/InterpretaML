import os
import sys
import re
import json
from datetime import datetime
import openai
from IA.ejemplos.query_ejemplos import Q_EJEMPLOS

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
from secret_key import API_KEY

USA_GPT4 = False
GPT_MODELO = "gpt-4" if USA_GPT4 else "gpt-3.5-turbo"
openai.api_key = API_KEY

def hacer_GPT_prompt (tema):
    # TODO: WILL maybe incontext learn
    # todo_ejemplos = '\n\n'.join (['Las palabras_claves de ejemplo para el tema de ' + q[0] + ' es : ' + q[1] for q in Q_EJEMPLOS.items()])
    system_prompt = 'Mostras todas sus respuestas en una lista separada por comas' 
    user_prompt = f'Quiero generar palabras clave y hashtags que puedan usarse en una discusión de Twitter sobre el tema de {tema}'

    prompt = [ {
        "role": "system",
        "content": system_prompt
    },{
        "role": "user",
        "content": user_prompt
    }]
    return prompt

def generar_palabras_claves (tema):
    """Generar palabras_claves con 'in-context learning'"""
    print ('Generando palabras claves')

    # Pregunta GPT con ejemplos
    result = openai.ChatCompletion.create(
                model=GPT_MODELO,
                messages= hacer_GPT_prompt (tema),
                temperature=0.9
            )
    response = result['choices'][0]['message']['content']

    hashtags = re.findall(r"#\S+", response)
    now = datetime.now()
    with open(f'IA/logs/hashtags{now}.json', "w") as outfile:
        json.dump(hashtags, outfile)

    return hashtags