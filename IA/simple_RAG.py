import os
import sys
import openai
from datetime import datetime
import json

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
from secret_key import API_KEY

USA_GPT4 = True
GPT_MODELO = "gpt-4" if USA_GPT4 else "gpt-3.5-turbo"
openai.api_key = API_KEY

def simple_RAG (tema, query, ejemplos):
    print ('Mejorando el query')
    system_prompt = f"""Estoy llevando a cabo un análisis sobre el discurso público en torno a {tema}. El query actual que tengo captura un alcance básico de los tweets relacionados con el tema, pero quiero refinarla para abarcar un conjunto de tweets más amplio y diverso que refleje diferentes puntos de vista, hashtags y demográficos. Adjunto los parámetros del query existente y un conjunto tweets de muestra. No corta el query actual. Solo agrega complejidad. Responde solo con el query nuevo, nada más. Puede usa estas operaciones booleanas AND, NOT, OR, (). A veces, puede usar NEAR/n como un operador de proximidad que incluye frases dentro de n palabras.
                    Debes usar el regex *, (por ejemplo: aprobad*), si el final de una palabra es flexible. Debes usar ?, (por ejemplo: rid?culo), si la letra es flexible.
                    Separe la consulta en secciones y etiquete cada una. Coloque las etiquetas entre <<< y >>>."""
    user_prompt = f'Aquí está el query:\n {query} \n\n Aquí están los tweet:\n {ejemplos}'

    prompt = [ {
        "role": "system",
        "content": system_prompt
    },{
        "role": "user",
        "content": user_prompt
    }]

    result = openai.ChatCompletion.create(
                model=GPT_MODELO,
                messages= prompt,
                temperature=0.7
            )
    response = result['choices'][0]['message']['content']

    primer_comentario_idx = response.index ('<<<')
    primer_booleana_idx = response.index ('(')
    # Si hay un error aquí, es un problema de GPT
    consulta_inicio_idx = min (primer_comentario_idx, primer_booleana_idx)

    consulta = response[consulta_inicio_idx:]

    now = datetime.now()
    with open(f'IA/logs/RAG{now}.json', "w") as outfile:
        json.dump(consulta, outfile)

    return consulta