import os
import sys
import openai
from IA.ejemplos.query_ejemplos import Q_EJEMPLOS
from datetime import datetime
import json

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
from secret_key import API_KEY

USA_GPT4 = True
GPT_MODELO = "gpt-4" if USA_GPT4 else "gpt-3.5-turbo"
openai.api_key = API_KEY

def hacer_GPT_prompt_sin_RAG (tema):
    todo_ejemplos = '\n\n'.join (['Una consulta de ejemplo para el tema de ' + q[0] + ' es : ' + q[1] for q in Q_EJEMPLOS.items()])
    system_prompt = """Quiero hacer un query con un algoritmo booleano para consultar Tweets sobre un tema específico. Quiero que el query contenga una amplia gama de puntos de vista, perspectivas, hashtags y datos demográficos.
                    Puede usa estas operaciones booleanas AND, NOT, OR, (). A veces, puede usar NEAR/n como un operador de proximidad que incluye frases dentro de n palabras.
                    Debes usar el regex *, (por ejemplo: aprobad*), si el final de una palabra es flexible. Debes usar ?, (por ejemplo: rid?culo), si la letra es flexible.
                    Separe la consulta en secciones y etiquete cada una. Coloque las etiquetas entre <<< y >>>. Aquí hay unos ejemplos.
                    \n""" +  todo_ejemplos
    user_prompt = f'Generas una consulta para el tema de {tema}.'

    prompt = [{
        "role": "system",
        "content": system_prompt
    }, {
        "role": "user",
        "content": user_prompt
    }]
    return prompt

def generar_primera_consulta (tema):
    """Generar la primera consulta con 'in-context learning' sin datos de Twitter"""
    print ('Generando la primera consulta')

    # Pregunta GPT con ejemplos
    result = openai.ChatCompletion.create(
                model=GPT_MODELO,
                messages= hacer_GPT_prompt_sin_RAG (tema),
                temperature=0.7
            )
    response = result['choices'][0]['message']['content']

    primer_comentario_idx = response.index ('<<<')
    primer_booleana_idx = response.index ('(')
    # Si hay un error aquí, es un problema de GPT
    consulta_inicio_idx = min (primer_comentario_idx, primer_booleana_idx)

    consulta = response[consulta_inicio_idx:]

    now = datetime.now()
    with open(f'IA/logs/q1{now}.json', "w") as outfile:
        json.dump(consulta, outfile)

    return consulta

